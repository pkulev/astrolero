import pygame
 
 
class GuiElement(object):
    def __init__(self, owner):
        self._owner = owner
        self._application = owner.owner
        self._font = None
         
    @property
    def owner(self):
        """State - owner of GUI element"""
        return self._owner
         
    @property
    def application(self):
        """Master application"""
        return self._application
         
    @property
    def font(self):
        """Current font. You can specify it's size"""
        return self._font
         
    @font.setter
    def font(self, size):
        self._font = pygame.font.Font(None, size)
         
    def draw(self):
        raise NotImplementedError("All GUI element must specify draw method")
         
    def __call__(self, event):
        raise NotImplementedError('''All GUI elements
                                  must specify __call__ method''')
