import sys
from PygameBase import *
from CGame import *
from CEntity import *

AQUA      =  (  0, 255, 255)
BLACK     =  (  0,   0,   0)
BLUE      =  (  0,   0, 255)
FUCHSIA   =  (255,   0, 255)
GRAY      =  (128, 128, 128)
GREEN     =  (  0, 128,   0)
LIME      =  (  0, 255,   0)
MAROON    =  (128,   0,   0)
NAVYBLUE  =  (  0,   0, 128)
OLIVE     =  (128, 128,   0)
PURPLE    =  (128,   0, 128)
RED       =  (255,   0,   0)
SILVER    =  (192, 192, 192)
TEAL      =  (  0, 128, 128)
WHITE     =  (255, 255, 255)
YELLOW    =  (255, 255,   0)


class CShip(CEntity):
    def __init__(self):
        self.coord = Coord(None, None)
        self.constraints = Coord(None, None)
        self.direction = None #(THINK!)
        
        #THINK!
        self.speedX = None
        self.speedY = None


class PlayerShip(CShip):
    def __init__(self, startX, startY):
        self.coord = Coord(startX, startY)
        self.baseType = "PlayerShip"
        self.direction = None

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
