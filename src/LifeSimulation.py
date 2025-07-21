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
    world.update() # initialise each entity's initial state

    # selector initialisation
    selector = Selection(world, [[True for _ in range(world_size[0]//2)]+[False for _ in range(world_size[0]//2)] for _ in range(world_size[1])])

    # historian initialisation
    historian = Displays(folder, world)
    historian.export_round() # export the state of round 0

    print("Starting the simulation:")
    for _ in range(rounds):
        world.round += 1
        progress_bar(world.round, rounds)

        world.process()
        world.resolve_requests()
        historian.export_round() # historian recording the history
        world.update() # remove corpse

        selector.kill() # kill entities in the defined zone

    print(f'\nDone - Data exported to "{historian.directory}"')

    historian.gen_frames() # generating the frames for the video
    historian.gen_pop_graph() # generating the population graph
    historian.gen_video(fps)

    # Checks for overlapping in position
    checker = Checker("dev_sim_records")
    for state in checker.check_file():
        if state[1]:
            print(state)

if __name__ == '__main__':
    ROUNDS = 256
    FPS = 30 
    WORLD_SIZE = (64,64)
    POPULATION = 1024
    FOLDER = "dev_sim_records" # the repository to save all of the records

    main(WORLD_SIZE, POPULATION, ROUNDS, FOLDER, FPS)
    print("PROGRAM ENDED")
