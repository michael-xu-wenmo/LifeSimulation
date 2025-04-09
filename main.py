from world import World
from displays import Displays
import numpy as np

def main():
    ROUNDS = 256
    FPS = 30 
    WORLD_SIZE = (64,64)
    POPULATION = 1024
    FOLDER = "dev_sim_records" # the repository to save all of the records

    # world initialisation
    world = World(WORLD_SIZE)
    
    world.gen_pop_map(POPULATION) # generating the population distribution

    world.populate("Dummy") # creating the entities
    world.update() # initialise each entity's initial state

    # historian initialisation
    historian = Displays(FOLDER, world)
    historian.export_round() # export the state of round 0

    world(ROUNDS, historian) # running the simulation

    historian.gen_frames() # generating the frames for the video
    historian.gen_pop_graph() # generating the population graph
    historian.gen_video(FPS)

if __name__ == '__main__':
    main()
    print("PROGRAM ENDED")