from worldobj import World
from worldobj import Selection

from utilities import Displays
from utilities import progress_bar
from utilities import Checker

def main(world_size, population, rounds, folder, fps):

    # world initialisation
    world = World(world_size)
    
    world.gen_pop_map(population) # generating the population distribution

    world.populate("Dummy") # creating the entities
    world.update_sensors() # initialise each entity's initial state

    # selector initialisation
    selector = Selection(world, [[True for _ in range(world_size[0]//2)]+[False for _ in range(world_size[0]//2)] for _ in range(world_size[1])])

    # historian initialisation
    historian = Displays(folder, world)
    historian.export_round() # export the state of round 0

    # simulation stack
    print("Starting the simulation:")
    for _ in range(rounds):
        world.round += 1
        progress_bar(world.round, rounds)

        if world.round % 10 == 0:
            selector.kill() # kill entities in the defined zone
            selector.redistribute() # redistribute the entities

        world.update_attri_pos() # vital to keep track of where the entities are
        world.update_sensors()

        world.process()
        world.resolve_requests()

        historian.export_round() # historian recording the history
        
        world.update_deaths() # remove corpse (after round export to identify who died)

    print(f'\nDone - Data exported to "{historian.directory}"/rounds_json')

    historian.gen_frames() # generating frames for video
    historian.gen_pop_graph() # generating population graph
    historian.gen_video(fps)

    # Checks for overlap in position
    print("Collision Checker - Checking")
    good = True
    checker = Checker("dev_sim_records")
    for state in checker.check_file():
        if state[1]:
            good = False
            print(state)
    if good:
        print("Done - No collisions detected")
    else:
        print("Done - Collisions found")

if __name__ == '__main__':
    ROUNDS = 128
    FPS = 2
    WORLD_SIZE = (64,64)
    POPULATION = 2048
    FOLDER = "dev_sim_records" # the repository to save all of the records

    main(WORLD_SIZE, POPULATION, ROUNDS, FOLDER, FPS)