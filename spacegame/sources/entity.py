from .pygame_base import pygame

class Gizmo(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._width = 0
        self._height = 0

    def __str__(self):
        print ("({0}; {1})".format(self._x, self._y))

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
        
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        self._y = value
    
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value

class CEntity(Gizmo):
    def __init__(self):
        self._constraints = Gizmo(0, 0)
        self._baseType = None
        self._image = None

        self.visible = True
       
    @property
    def image(self):
        return self._image
    @image.setter
    def image(self, path):
        self._image = pygame.image.load(path)

    @property
    def baseType(self):
        return self._baseType
    @baseType.setter
    def baseType(self, value):
        self._baseType = value

    @property
    def constraints(self):
        return self._constraints
    @constraints.setter
    def constraints(self, value):
        self._constraints = value
