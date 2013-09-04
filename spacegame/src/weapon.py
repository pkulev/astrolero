from .core.entity import *

class Weapon(Entity):
    def __init__(self, wtype):
        super(Weapon, self).__init__(self)
        
    def fire(self):
        print("bang!")
