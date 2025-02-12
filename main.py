import setup

def main():
    world = setup.gen_world(128,128)
    print(world)

if __name__ == '__main__':
    main()
    print("Done")