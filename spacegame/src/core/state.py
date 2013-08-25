import pygame

class State(object):
    def __init__(self, owner):
        self._owner = owner

    @property
    def owner(self):
        """Application - owner of the state"""
        return self._owner
        
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
        
        self.background = None
    
        pygame.mixer.init()
       
    def addGameObject(self, gameObject):
        self._gameObjects.append(gameObject)

    def setBackground(self, path):
        self.background = pygame.image.load(path)
        
    def handleEvent(self, event):
        raise NotImplementedError("Should have implemented this function")

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: owner.exitGame()
            self.handleEvent(event)

    def updateState(self):
        for i in self._gameObjects:
            i.updateState()

    def drawScreen(self):
        self.owner.display.fill(pygame.Color(0,0,0,1))

        self.owner.display.blit(self.background, (0, 0))
        
        for i in self._gameObjects:
            self.owner.display.blit(i.image, (i.x, i.y))
