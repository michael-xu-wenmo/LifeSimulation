from world import World
from displays import Displays
import utilities

def main():
    ROUNDS = 240
    FPS = 30 
    WORLD_SIZE = (128,128)
    POPULATION = 128*128
    FOLDER = "dev_sim_records"

    world = World(WORLD_SIZE)
    world.gen_pop_map(POPULATION)
    world.populate("Dummy")
    world.update()

    historian = Displays(FOLDER, world)
    historian.export_round() # round 0

    world(ROUNDS, historian)

    historian.gen_frames()
    historian.gen_pop_graph()
    historian.gen_video(FPS)

if __name__ == '__main__':
    main()
    print("PROGRAM ENDED")