class Loc:

    def __init__(self, pos: tuple[int,int], entity, food):
        self.pos = pos
        self.entity = entity
        self.food = food
        # potential temperature attribute?
    
    def get_pos(self):
        return self.pos

    def get_food(self):
        return self.food
    
    def get_entity(self):
        return self.entity

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
        
    def remove_entity(self):
        self.entity = None
        return 1
    
    def add_entity(self, entity):
        if self.entity == None:
            self.entity = entity
            return 1
        else:
            return 0