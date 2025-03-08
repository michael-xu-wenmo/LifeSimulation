from organisms.entity import Entity
import random

# Dummy class. Reproduces asexually. No neuronetwork determining its actions.
class Dummy(Entity):

    def __call__(self):
        #x: float = random.random()
        #x: float = random.choice([-1,1]) * x
        #y: float = random.random()
        #y = random.choice([-1,1]) * y
        x = 1
        y = 0
        
        self.effectors["move"] = [x,y]
        return self.effectors

if __name__ == "__main__":
    test_dummy = Dummy("010101||||",(0,0))
    print(test_dummy.sensor_attri)
