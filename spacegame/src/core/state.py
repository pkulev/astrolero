import pygame
from pygame.locals import *
from .gui import *

class State(object):
    def __init__(self, owner):
        self._owner = owner
        self._background  = None
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
        return self._music
    @music.setter
    def music(self, path):
        self._music = pygame.mixer.music.load(path)

    def handleEvents(self):
        raise NotImplementedError("handleEvents method not implemented")

    def updateState(self):
        raise NotImplementedError("updateState method not implemented")

    def drawScreen(self):
        raise NotImplementedError("drawScreen method not implemented")

class InGame(State):

    def __init__(self, owner):
        super(InGame, self).__init__(owner)
        self._gameObjects = []
        
        pygame.mixer.init()
       
    def addGameObject(self, gameObject):
        self._gameObjects.append(gameObject)

    def handleEvent(self, event):
        raise NotImplementedError("Should have implemented this function")

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.owner.exitGame()
            self.handleEvent(event)

    def updateState(self):
        for i in self._gameObjects:
            i.updateState()

    def drawScreen(self):
        self.owner.display.fill(pygame.Color(0,0,0,1))
        self.owner.display.blit(self.background, (0, 0))
        for i in self._gameObjects:
            self.owner.display.blit(i.image, (i.x, i.y))

class MainMenu(State):
    def __init__(self, owner):
        super(MainMenu, self).__init__(owner)
        pygame.font.init()
        self._menus = []
        self._currentMenu = None

    def addMenu(self, caption, item_action_dict):
        new_menu = SubMenu(self, caption)
        for entry, action in item_action_dict.items():
            new_menu.addMenuItem(entry, action)
        self._menus.append(new_menu)

    def setCurrentMenu(self, caption):
        self._currentMenu = list(filter(lambda m: m.caption == caption,
                                        self._menus))[0]

    def handleEvents(self):
        if pygame.event.get([pygame.QUIT]): self.owner.exitGame()
        for event in pygame.event.get([pygame.KEYDOWN]):
            self._currentMenu.handleEvents(event)

    def updateState(self):
        pass

    def drawScreen(self):
        self.owner.display.fill(pygame.Color(0, 0, 0, 1))
        self.owner.display.blit(self.background, (0, 0))
        self._currentMenu.draw()
            

