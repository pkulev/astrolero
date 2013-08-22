import sys

from .game import *
from .entity import *

class CShip(CEntity):
    def __init__(self):
        self.coord = Coord(None, None)
        self.constraints = Coord(None, None)
        self.direction = None #(THINK!)
        
        self.speedX = None
        self.speedY = None

class PlayerShip(CShip):
    def __init__(self, startX, startY):
        self.coord = Gizmo(startX, startY)
        self.baseType = "PlayerShip"
        self.direction = None

    def updateState(self):
        self.updatePosition()

    def updatePosition(self):
        if self.direction == "up":
            self.setY(self.getY() - 25)
            if self.getY() < 0:
                self.setY(0)
#            self.direction = None
        elif self.direction == "down":
            self.setY(self.getY() + 25)
            if self.getY() + self.get_height() >= self.constraints.getHeight():
                self.setY(self.constraints.getHeight() - self.get_height())
#            self.direction = None
        elif self.direction == "right":
            self.setX(self.getX() + 25)
            if self.getX() + self.get_width() >= self.constraints.getWidth():
                self.setX(self.constraints.getWidth() - self.get_width())
#            self.direction = None
        elif self.direction == "left":
            self.setX(self.getX() - 25)
            if self.getX() <= 0:
                self.setX(0)
#            self.direction = None
        else:
            pass

class EnemyShip(CShip):
    def __init__(self, startX, startY):
        self.baseType = "EnemyShip"
