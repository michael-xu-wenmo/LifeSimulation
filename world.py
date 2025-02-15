from loc import Loc
import organisms

import numpy as np
from numpy import random

def _gen_genome(chromosomes: int):
    """a generator to give randomly assign an integer (0,256) to correspond to a chromosome"""
    cc = 0
    while cc < chromosomes:
        yield random.randint(0,256)
        cc += 1


class World():
    def __init__(self, width, height):
        self.round = 0

        self.width = width
        self.height = height
        self.locs = np.array([[Loc((x,y)) for x in range(width)] for y in range(height)])
        self.entities = []
        self.population = len(self.entities)

    # export internal state to a dictionary
    def export(self):
        inner_state = {
            "round": self.round,
            "population": self.population,
            "entities": list(map(lambda entity: (entity.get_genome().hex(),entity.get_pos()),self.entities))
        }
        return inner_state

    # setup fuctions
    def gen_pop_map(self, population):
        """generated a psuedorandom distribution map of the entities"""
        if population <= self.width * self.height:
            self.init_pop_map = [ True for _ in range(population)]
            self.init_pop_map += [False for _ in range(self.width*self.height - population)]
            self.init_pop_map = np.array(self.init_pop_map)
            random.shuffle(self.init_pop_map)
            self.init_pop_map = self.init_pop_map.reshape(self.height,self.width)
    
    def populate(self, entity_chromosomes):
        """Populate the world with the given distribution map"""
        for row in range(self.height):
            for column in range(self.width):
                if self.init_pop_map[row][column]: # type: ignore
                    entity = organisms.Dummy_entity(bytes(_gen_genome(entity_chromosomes)),(column, row))
                    
                    success = self.locs[row][column].add_entity(entity)
                    if success:
                        self.entities.append(entity)
                    else:
                        del entity
        self.population = len(self.entities)

    def gen_food(self, number, distribution):
        # return the inital set of foods.
        return