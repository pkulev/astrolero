import sys

from .core.entity import *


class Ship(Entity):
    def __init__(self):
        super(Ship, self).__init__(None)


class PlayerShip(Ship):
    def __init__(self, startX, startY):
        super(PlayerShip, self).__init__()
        self._x = startX
        self._y = startY
        self.baseType = "PlayerShip"

    def updateState(self):
        self.updatePosition()

    def updatePosition(self):
        pass


class EnemyShip(Ship):
    def __init__(self, startX, startY):
        super(EnemyShip, self).__init__()
        self.baseType = "EnemyShip"
