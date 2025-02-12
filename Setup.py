from loc import Loc

import numpy as np
from numpy import random

def gen_world(width,height):
    '''Generate the simulation world with the given width and height. Returns a 2D array of Loc objects'''

    world = np.array([[Loc((x,y),None,None) for x in range(width)] for y in range(height)])

    # return a 2D array of Loc objects
    return world

def populate(world, entities):
    return

def gen_food(world, number, distribution):
    # return the inital set of foods.
    return