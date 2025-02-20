from organisms.entity import Entity

class Loc:
    # a class used to regulate the an entity.
    def __init__(self, pos):
        self.POS = pos
        self.entity : Entity|None = None
        self.food = None
        # potential temperature attribute?

        self.requests: dict[str,list[Entity]] = {"move":[], "kill":[], "reproduce":[], "eat":[]}
        self.deserved: dict[str,list[Entity]] = {"move":[], "kill":[], "reproduce":[], "eat":[]}

    # actions
    def add_entity(self, entity: Entity):
        if self.entity == None:
            self.entity = entity
            return True
        else:
            return False
    
    def remove_entity(self):
        self.entity = None
        return True
    
    def remove_food(self):
        if self.food != None:
            del self.food
            self.food = None
            return True
        else:
            return False
    
    def add_food(self, food):
        if self.food == None:
            self.food = food
            return True
        else:
            return False
    
    # methods used to set the entity's inputs
    def give_pos(self):
        try:
            weight = self.entity.get_sensor_attri("global_position") # type: ignore
            if weight >= 128:
                self.entity.receive("global_position", [self.POS]) # type: ignore
            return True
        
        except AttributeError:
            return False
    
    def give_entity(self):
        return
    
    def give_food(self):
        return 

    # requests done to the Loc
    def request(self, req_type: str, entity: Entity):
        self.requests[req_type].append(entity)

    # resolve the requests and determines who die
    def resolve_move(self, entities: list[Entity]):
        deserved = entities[0]
        for entity in entities:
            if entity.get_points() > deserved.get_points():
                deserved = entity
        self.deserved["move"] = [deserved]

    def respond(self):
        self.deserved: dict[str,list[Entity]] = {"move":[], "kill":[], "reproduce":[], "eat":[]}
        for request, entities in self.requests.items():
            if entities == []:
                continue
            getattr(self, f"resolve_{request}")(entities)
        self.requests: dict[str,list[Entity]] = {"move":[], "kill":[], "reproduce":[], "eat":[]} #refresh the request lists
        return self.deserved