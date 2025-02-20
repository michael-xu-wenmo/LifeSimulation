from organisms.entity import Entity
import random

# Dummy class. Reproduces asexually. No neuronetwork determining its actions.
class Dummy(Entity):

    def __call__(self):
        
        return self.effectors

if __name__ == "__main__":
    test_dummy = Dummy("010101||||",(0,0))
    print(test_dummy.sensor_attri)
