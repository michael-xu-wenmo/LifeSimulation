import setup

def main():
    world = setup.gen_world(128,128)
    pop_map = setup.gen_pop_map(world, 1000)
    print(pop_map)

if __name__ == '__main__':
    main()
    print("Done")