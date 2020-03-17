import pygame

from eaf.state import State


class IngameState(State):

    def addGameObject(self, gameObject):
        self._gameObjects.append(gameObject)

    def handleEvent(self, event):
        raise NotImplementedError("Should have implemented this function")

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.stop()
            self.handleEvent(event)

    def updateState(self):
        raise NotImplementedError("Should have implemented this function")

    def drawScreen(self):
        self.owner.display.fill(pygame.Color(0, 0, 0, 1))
        self.owner.display.blit(self.background, (0, 0))
        for i in self._gameObjects:
            self.owner.display.blit(i.image, (i.x, i.y))
