from world import World
from displays import Displays
import utilities

def main():
    ROUNDS = 10
    FPS = 30 
    WORLD_SIZE = (128,128)
    POPULATION = 10

    world = World(WORLD_SIZE)

    world.gen_pop_map(POPULATION)
    world.populate("Dummy")
    world.update()

    historian = Displays("dev_sim_records", world)
    historian.export_round() # round 0

    print("SIMULATION STARTED...")
    for _ in range(ROUNDS):
        world.round += 1
        utilities.progress_bar(world.round, ROUNDS)

        # 1. all entities process their effectors
        world.process()
        # 2. resolve all requests
        world.resolve_requests()
        # 3. update world status
        world.update()
        # 4. historian export the current world state
        historian.export_round()

    print("\nSIMULATION ENDED")

    # historian record the history
    historian.gen_frames()
    historian.gen_pop_graph()

if __name__ == '__main__':
    main()
    print("PROGRAM ENDED")