from loc import Loc
from entity import Entity

import numpy as np
from numpy import random

def gen_world(width,height):
    '''Generate the simulation world with the given width and height. Returns a 2D array of Loc objects'''

    world = np.array([[Loc((x,y)) for x in range(width)] for y in range(height)])

    # return a 2D array of Loc objects
    return world

def gen_pop_map(world, population):
    width, height = world.shape
    if population <= width*height:
        entity_list = [ True for _ in range(population)]
        entity_list += [False for _ in range(width*height - population)]
        entity_list = np.array(entity_list)
        random.shuffle(entity_list)
        entity_list = entity_list.reshape(height,width)
        return entity_list
    return np.array([])


def populate(world, map):
    pass

def gen_food(world, number, distribution):
    # return the inital set of foods.
    return