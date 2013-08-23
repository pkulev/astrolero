import sys

from .core.entity import *

class CShip(CEntity):
    def __init__(self):
        super(CShip, self).__init__(None)

class PlayerShip(CShip):
    def __init__(self, startX, startY):
        super(PlayerShip, self).__init__()
        self.x = startX
        self.y = startY
        self.baseType = "PlayerShip"

    def updateState(self):
        self.updatePosition()

    def updatePosition(self):
        pass

class EnemyShip(CShip):
    def __init__(self, startX, startY):
        super(EnemyShip, self).__init__()
        self.baseType = "EnemyShip"
