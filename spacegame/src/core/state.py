import pygame
from pygame.locals import *
from .gui import *


class State(object):
    def __init__(self, owner):
        self._owner = owner
        self._background = None
        self._music = None

    @property
    def owner(self):
        """Application - owner of the state"""
        return self._owner

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, path):
        self._background = pygame.image.load(path)

    @property
    def music(self):
        """Contains current music file path"""
        return self._music

    @music.setter
    def music(self, path):
        pygame.mixer.music.load(path)
        self._music = path

    def play_music(self):
        pygame.mixer.music.play(-1)

    def handleEvents(self):
        raise NotImplementedError("handleEvents method not implemented")

    def updateState(self):
        raise NotImplementedError("updateState method not implemented")

    def drawScreen(self):
        raise NotImplementedError("drawScreen method not implemented")
