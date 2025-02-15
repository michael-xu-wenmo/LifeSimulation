from world import World
from displays import Displays

def main():
    ROUNDS= 120
    FPS = 30 
    WORLD_SIZE = (128,128)
    POPULATION = 1000
    LIFE_CHROMOSOMES = 16


    print("Initialising the world...")
    world = World(WORLD_SIZE[0],WORLD_SIZE[1])

    print("Populating the world...")
    world.gen_pop_map(POPULATION)
    world.populate(LIFE_CHROMOSOMES)

    print("Exporting initial world state...")
    historian = Displays("dev_sim_records", world)
    historian.export_round() # round 0

    print("Start Simulating...")
    while world.round < ROUNDS:
        ### Some how I have to make this O(n) time. n is the population###
        # 1. update all entities
        # 2. all entities process their effectors
        # 3. send requests to Locs with their effectors output
        # 4. resolve all requests
        # 5. historian export the current world state

        world.round += 1

    print("Simulation Ended")

    print("Generating frames...")
    historian.gen_frames()

if __name__ == '__main__':
    main()
    print("Done")