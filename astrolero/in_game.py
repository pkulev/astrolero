import pygame

from .core.state import State


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
            if event.type == pygame.QUIT: 
                self.owner.exitGame()
            self.handleEvent(event)

    def updateState(self):
        raise NotImplementedError("Should have implemented this function")

    def drawScreen(self):
        self.owner.display.fill(pygame.Color(0, 0, 0, 1))
        self.owner.display.blit(self.background, (0, 0))
        for i in self._gameObjects:
            self.owner.display.blit(i.image, (i.x, i.y))
