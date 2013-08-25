from .Classes import *
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

class CGame(State):

    def __init__(self, owner):
        super(CGame, self).__init__(owner)
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

class Application(object):
    def __init__(self, caption):
        pygame.display

        self._state = None
        self.states = {}
        
        self.FPS = 60
        self.fpsClock = pygame.time.Clock()
        
        self.width = 640
        self.height = 480
        self.depth = 32
        self.caption = caption

        self.fullscreen = 0

        self.display = self.createWindow()

    def createWindow(self):
        display = pygame.display.set_mode((self.width, self.height),
                                          self.fullscreen, 
                                          self.depth)
        pygame.display.set_caption(self.caption)
        return display

    def exitGame(self):
        pygame.quit()
        sys.exit()

    @property
    def state(self):
        """Current application state.
           Raises KeyError on attempt to set state, which 
           has not been added via addState method.
        """
        return self._state

    @state.setter
    def state(self, name):
        if name in self.states.keys():
            self._state = self.states[name]
        else:
            raise KeyError("There is no state with name {0}".format(name))

    def addState(self, stateClass, name):
        self.states[name] = stateClass(self)
        
    def start(self):
        while True:
            self.state.handleEvents()
            self.state.updateState()
            self.state.drawScreen()
            
            pygame.display.update()
            self.fpsClock.tick(self.FPS)
