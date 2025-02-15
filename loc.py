class Loc:

    def __init__(self, pos):
        self.POS = pos
        self.entity = None
        self.food = None

        self.move_requests = []
        # potential temperature attribute?

    # god functions
    def add_entity(self, entity):
        if self.entity == None:
            self.entity = entity
            return 1
        else:
            return 0
    
    def remove_entity(self):
        self.entity = None
        return 1
    
    def remove_food(self):
        if self.food != None:
            del self.food
            self.food = None
            return 1
        else:
            return 0
    
    def add_food(self, food):
        if self.food == None:
            self.food = food
            return 1
        else:
            return 0
    
    # methods used by the entity to get the Loc's data
    def get_pos(self):
        return self.POS
    
    def get_entity(self):
        return self.entity
    
    def get_food(self):
        return self.food

    # requests done to the Loc
    def kill_request(self, attacker):
        pass

    def eat_request(self, eater):
        pass

    def move_request(self, entity):
        pass

    # resolve the requests and determines who die
    def respond(self):
        pass