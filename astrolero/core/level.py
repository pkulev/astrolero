import pygame
from .entity import *


class AbstractLevel(object):
    def __init__(self, owner):
        self._owner = owner

    def start(self):
        raise NotImplementedError("Cannot start abstract level instance")

    @property
    def owner(self):
        """Owner of the level (state)"""
        return self._owner
        
