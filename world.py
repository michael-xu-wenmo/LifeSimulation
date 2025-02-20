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
        self.locs= np.array([[Loc((x,y)) for x in range(self.width)] for y in range(self.height)])
        self.entities: set[Entity] = set()
        self.occupied_locs: list[Loc] = []
        self.requested_locs: list[Loc] = []
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
    
    def update(self):
        """update each entities' receptor"""
        self.occupied_locs: list[Loc] = list(map(lambda entity: self.locs[(entity.get_pos()[1],entity.get_pos()[0])],self.entities))
        for loc in self.occupied_locs:
            loc.give_pos() # update the "global_position" sensor

    # request senders
    def request_move(self, entity: Entity, data: list):
        max_range: int = entity.get_effectors_attri("move")
        new_x = entity.get_pos()[0] + round(data[0]*max_range)
        new_y = entity.get_pos()[1] + round(data[1]*max_range)
        try:
            self.locs[(new_y,new_x)].request("move",entity) # type: ignore
            self.requested_locs.append(self.locs[(new_y,new_x)]) # type: ignore
        except IndexError:
            pass

    def move(self, entities: list[Entity], target_loc: Loc):
        entity = entities[0]
        current_loc = self.locs[(entity.get_pos()[1],entity.get_pos()[0])]
        current_loc.remove_entity()
        target_loc.add_entity(entity)
        entity.pos = target_loc.POS

    def process(self):
        """pass data through each entity's processor and link it to the corresponding loc"""
        for loc in self.occupied_locs:
            entity = loc.entity # process its actions
            if entity == None:
                continue
            requests = entity()
            for request, data in requests.items():
                if data == []:
                    continue
                getattr(self, f"request_{request}")(entity,data)

    def resolve_requests(self):
        """resolve each request in each loc"""
        for loc in self.requested_locs:
            deserved = loc.respond()
            for request, data in deserved.items():
                if data == []:
                    continue
                getattr(self, request)(data, loc)