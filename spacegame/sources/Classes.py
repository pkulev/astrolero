import pygame
import sys
from pygame.locals import *
from pygame import K_w, K_a, K_s, K_d, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_ESCAPE as K_ESC
from CGame import *

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

class Coord(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        print "({0}; {1})".format(self.x, self.y)
        
    def getXY(self):
        return (self.x, self.y)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    def setXY(self, x, y):
        self.x = x
        self.y = y

    def setWidth(self, x):
        self.x = x
    def setHeight(self, y):
        self.y = y

    def getWidth(self):
        return self.x
    def getHeight(self):
        return self.y

class Entity(object):
    def __init__(self):
        self.coord = Coord(None, None)
        self.type = None
        self.visible = True #?
        self.image = None
        
    def init(args): #?
        pass

    def getX(self):
        return self.coord.getX()
    def getY(self):
        return self.coord.getY()
    def getXY(self):
        return self.coord.getXY()
    
    def setX(self, x):
        self.coord.setX(x)
    def setY(self, y):
        self.coord.setY(y)
    def setXY(self, x, y):
        self.coord.setXY(x, y)

    def setImage(self, path):
        self.image = pygame.image.load(path)
    def getImage(self):
        return self.image

    def get_height(self):
        return self.image.get_height()
    def get_width(self):
        return self.image.get_width()

class Movable(Entity):
    def __init__(self):
        self.coord = Coord(None, None)
        self.direction = None
        self.constraints = Coord(None, None)

    def setConstraints(self, x, y):
        self.constraints = Coord(x, y)

    def updatePosition(self):
        pass

class Immovable(Entity):
    def __init__(self):
        self.coord = Coord(None, None)
        
class Controller(object):
    def __init__(self):
        pass
    def getKey(self):
        pass

    
class PlayerShip(Movable):
    def __init__(self, startX, startY):
        self.coord = Coord(startX, startY)
        self.type = "PlayerShip"
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

        
class Background(Immovable):
    def __init__(self, X, Y):
        self.coord = Coord(X, Y)
        self.type = "Background"
    def init(args):
        pass

