import pygame
from pygame.locals import *

from .core.hud_abstract import HudElement


class Bar(HudElement):
    def __init__(self, owner, value):
        super(Bar, self).__init__(owner)
        self._value = value
        self._font = 24
        self._border = pygame.Rect(0, 0, 120, 25)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    def draw(self, pos_x, pos_y):
        value = self._font.render(str(self._value), 1, (255, 255, 255, 255))
        valpos = value.get_rect()
        
