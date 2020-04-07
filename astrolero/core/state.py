import pygame


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
        raise NotImplementedError

    def updateState(self):
        raise NotImplementedError

    def drawScreen(self):
        raise NotImplementedError
