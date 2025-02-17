from loc import Loc
import organisms

import numpy as np
from numpy import random


class World:

    @staticmethod
    def gen_genome():
        receptor = bytes([random.randint(0,256) for _ in range(3)]).hex()
        input_layor = bytes([random.randint(0,256) for _ in range(0)]).hex()
        hidden_layor = bytes([random.randint(0,256) for _ in range(0)]).hex()
        output_layor = bytes([random.randint(0,256) for _ in range(0)]).hex()
        effector = bytes([random.randint(0,256) for _ in range(3)]).hex()
        return f"{receptor}|{input_layor}|{hidden_layor}|{output_layor}|{effector}"

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
            "entities": list(map(lambda entity: (entity.get_genome(),entity.get_pos()),self.entities))
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
    
    def set_pop_map(self, distribution):
        self.init_pop_map = distribution

    def populate(self, type:str, disabled = []):
        """Populate the world with the given distribution map"""
        for row in range(self.height):
            for column in range(self.width):
                if self.init_pop_map[row][column]: # type: ignore
                    entity  = getattr(organisms, type)(World.gen_genome(), (column,row), disabled)
                    
                    success = self.locs[row][column].add_entity(entity)
                    if success:
                        self.entities.append(entity)
                    else:
                        del entity
        self.population = len(self.entities)

    def gen_food(self, number, distribution):
        # return the inital set of foods.
        return
    
    # world regulation funcs