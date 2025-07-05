from worldobj.world import World # for typing

class Selection:

    def __init__(self, world: World, zone):
        self.world = world
        self.zone = zone

    def kill(self):
        selected = self.world.locs[self.zone]
        for loc in selected:
            loc.kill_entity()