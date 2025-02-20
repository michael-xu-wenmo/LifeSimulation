from loc import Loc
import organisms
from organisms.entity import Entity # only for typing

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

    def __init__(self, dim: tuple[int,int]):
        print("INITIALISING THE WORLD...")
        self.round = 0

        self.width = dim[0]
        self.height = dim[1]
        self.locs = np.array([[Loc((x,y)) for x in range(self.width)] for y in range(self.height)])
        self.entities: set[Entity] = set()
        self.population = len(self.entities)
        print("FINISHED INITIALISING")

    # export internal state to a dictionary
    def export(self):
        inner_state = {
            "round": self.round,
            "population": self.population,
            "entities": list(map(lambda entity: (entity.get_genome(),entity.get_pos()),self.entities))
        }
        return inner_state

    # setup methods
    def gen_pop_map(self, population: int):
        """generated a psuedorandom distribution map of the entities"""
        print("GENERATING POPULATION MAP...")
        if population <= self.width * self.height:
            self.init_pop_map = [ True for _ in range(population)]
            self.init_pop_map += [False for _ in range(self.width*self.height - population)]
            self.init_pop_map = np.array(self.init_pop_map)
            random.shuffle(self.init_pop_map)
            self.init_pop_map = self.init_pop_map.reshape(self.height,self.width)
        print("FINSIHED GENERATING")
    
    def set_pop_map(self, distribution):
        self.init_pop_map = distribution

    def populate(self, type:str, disabled = []):
        print("POPULATING THE WORLD...")
        """Populate the world with the given distribution map"""
        for row in range(self.height):
            for column in range(self.width):
                if self.init_pop_map[row][column]: # type: ignore
                    entity  = getattr(organisms, type)(World.gen_genome(), (column,row), disabled)
                    
                    success = self.locs[row][column].add_entity(entity)
                    if success:
                        self.entities.add(entity)
                    else:
                        del entity
        self.population = len(self.entities)
        print("FINISHED POPULATING")

    def gen_food(self, number, distribution):
        # return the inital set of foods.
        return
    
    # simulation methods
    
    def update_receptor(self):
        """update each entities' receptor"""
        occupied_locs: list[Loc] = list(map(lambda entity: self.locs[(entity.get_pos()[1],entity.get_pos()[0])],self.entities))
        for loc in occupied_locs:
            loc.give_pos() # update the "global_position" sensor

    def update_process(self):
        """pass data through each entity's processor and link it to the corresponding loc"""
        for entity in self.entities:
            entity() # process its actions

    def resolve_requests(self):
        """resolve each request in each loc"""

        pass