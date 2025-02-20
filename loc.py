from organisms.entity import Entity

class Loc:
    # a class used to regulate the an entity.
    def __init__(self, pos):
        self.POS = pos
        self.entity : Entity|None = None
        self.food = None

        self.move_requests = []
        # potential temperature attribute?

    # god functions
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
    def reproduce_request(self, parent):
        pass

    def kill_request(self, attacker):
        pass

    def eat_request(self, eater):
        pass

    def move_request(self, entity):
        pass

    # resolve the requests and determines who die
    def respond(self):
        pass