from worldobj.world import World # for typing

import numpy

class Selection:

    def __init__(self, world: World, zone):
        self.world = world
        self.zone = zone

    def kill(self):
        selected = self.world.locs[self.zone]
        for loc in selected:
            loc.kill_entity()
    
    def redistribute(self):
        # shuffling the positions of the entities randomly
        world_map = numpy.array(list((map(lambda loc: loc.remove_entity(), self.world.locs.flatten())))) # the locs should be emptied now
        numpy.random.shuffle(world_map)
        world_map.resize((self.world.height, self.world.width))

        # reasigning the entities to the emptied locs
        for row in range(len(world_map)):
            for column in range(len(world_map[row])):
                self.world.locs[row][column].add_entity(world_map[row][column])