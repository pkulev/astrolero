from .core.level import AbstractLevel
from .game_entities import Asteroid
from .in_game import InGame


class AsteroidBeltLevel(AbstractLevel):
    def __init__(self, owner):
        #owner must be an instance of InGame state
        assert(type(owner) == InGame)
        super(AsteroidBeltLevel, self).__init__(owner)

    def start(self):
        pass

