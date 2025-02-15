from world import World
from displays import Displays

def main():

    print("Initialising the world...")
    world = World(128,128)

    print("Populating the world...")
    world.gen_pop_map(1000)
    world.populate(16)

    print("Exporting initial world state...")
    historian = Displays("dev_sim_records", world)
    historian.export_round()

    print("Start Simulating...")

    print("Simulation Ended")

    print("Generating frames...")
    historian.gen_frames()

if __name__ == '__main__':
    main()
    print("Done")