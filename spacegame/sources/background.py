from .entity import *

class CBackground(CEntity):
    def __init__(self, X, Y):
        self.coord = Coord(X, Y)
        self.type = "Background"
    def init(args):
        pass
