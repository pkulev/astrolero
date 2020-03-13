import pygame


class HudElement(object):
    def __init__(self, owner):
        self._owner = owner
        self._application = owner.owner
        self._font = None
         
    @property
    def owner(self):
        """State - owner of HUD element"""
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
        raise NotImplementedError("All HUD element must specify draw method")
