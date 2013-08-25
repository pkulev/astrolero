import pygame

class Gizmo(object):
    """Represents bounding box for every in-game object.
       Can also be used for defining constarints.
    """
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._width = 0
        self._height = 0

    def __str__(self):
        print ("({0}; {1})".format(self._x, self._y))

    @property
    def x(self):
        """Horizontal coordinate of top left corner"""
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
        
    @property
    def y(self):
        """Vertical coordinate of top left corner"""
        return self._y
    @y.setter
    def y(self, value):
        self._y = value
    
    @property
    def width(self):
        """Bounding box width"""
        return self._width
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        """Bounding box height"""
        return self._height
    @height.setter
    def height(self, value):
        self._height = value

class CEntity(Gizmo):
    """Base class for all in-game objects.
       Defines position, size, constraints (if present),
       visibility, image and type of game object.
    
    Provides pure abstract methods for updating state of object.
    """
    
    def __init__(self, owner = None):
        super(CEntity, self).__init__(0, 0)
        self._owner = owner 
        self._constraints = Gizmo(0, 0)
        self._baseType = None
        self._image = None

        self.visible = True
       
    @property
    def owner(self):
        """Read only.
           Entity owner - RM or game object"""
        return self._owner
        
    @property
    def image(self):
        """Pygame image"""
        return self._image
    @image.setter
    def image(self, path):
        self._image = pygame.image.load(path)
        self._width = self._image.get_width()
        self._height = self._image.get_height()

    @property
    def baseType(self):
        """Homebrew RTTI field.
           Probably will be removed in the future.
        """
        return self._baseType
    @baseType.setter
    def baseType(self, value):
        self._baseType = value

    @property
    def constraints(self):
        """Bounding box, defining allowed positions of movable objects.
           Will be moved to 'Movable' class in the future"""
        return self._constraints
    @constraints.setter
    def constraints(self, value):
        self._constraints = value

    def updateState(self):
        """Virtual function for updating state of an object
           at each iteration of game cycle
        """
        raise NotImplementedError("updateState function was not implemented")