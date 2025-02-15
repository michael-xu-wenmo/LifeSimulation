from organisms.entity import Entity
import random

class Dummy_entity(Entity):
    def __init__(self, genome: bytes, init_pos):
        self.genome = genome
        self.pos = init_pos
        super(Entity).__init__()
    
    def process(self):
        # move randomly
        d_x = random.randint(-1,1)
        d_y = random.randint(-1,1)
        x = random.randint(0,self.SPEED) * d_x
        y = random.randint(0,self.SPEED) * d_y
        self.act_eff_neu['move'] = (x,y)
        return self.act_eff_neu