#from organisms.entity import Entity
from entity import Entity

import numpy as np
import torch
import torch.nn as nn

class Linearus(Entity, nn.Module):
    '''An entity that uses a linear neural network to determine its actions. It has a genome that defines the structure of the network.'''

    def __init__(self, genome: str, pos: tuple[int,int], disabled = []):
        super(Linearus, self).__init__(genome, pos, disabled)

    def __call__(self) -> dict[str, list]: #type: ignore
        '''Returns the effectors of the entity. This is where the neural network processes the input from the sensors and generates the output.'''
        pass

if __name__ == "__main__":
    DEVICE = "cpu" #"mps"

    test_linearus = Linearus("010101||||",(0,0)).to(device=DEVICE)
    print(test_linearus.sensor_attri)