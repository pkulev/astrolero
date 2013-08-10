from PygameBase import pygame

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

class CEntity(object):
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
