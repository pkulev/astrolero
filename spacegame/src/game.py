from .Classes import *
import pygame

class State(object):
    def handleEvents(self):
        raise NotImplementedError("handleEvents method not implemented")

    def updateState(self):
        raise NotImplementedError("updateState method not implemented")

    def drawScreen(self):
        raise NotImplementedError("drawScreen method not implemented")

class CGame(State):

    def __init__(self, caption):
        self.FPS = 60
        self.fpsClock = pygame.time.Clock()
        
        self.width = 640
        self.height = 480
        self.depth = 32

        self.fullscreen = 0

        self.display = self.createWindow(self.width, self.height, 
                                         self.fullscreen, self.depth, 
                                         caption) 

        self._gameObjects = []
        self._prevGOlist = [] #added for filter spam

        #background
        self.bg = None
    
        pygame.mixer.init()
       
    def addGameObject(self, gameObject):
        self._gameObjects.append(gameObject)

    def setBackground(self, path):
        self.bg = pygame.image.load(path)
        
    def createWindow(self, width, height, fullscreen, depth, 
                     caption="game"):
        pygame.init()
        display = pygame.display.set_mode((width, height), fullscreen, depth)
        pygame.display.set_caption(caption)
        return display

    def exitGame(self):
        pygame.quit()
        sys.exit()

    def handleEvent(self, event):
        raise NotImplementedError("Should have implemented this function")

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == 'QUIT': self.exitGame()
            self.handleEvent(event)

    def updateState(self):
        for i in self._gameObjects:
            i.updateState()

    def drawScreen(self):
        if self._prevGOlist != self._gameObjects:
            print(self._gameObjects)
            self._prevGOlist = self._gameObjects[:]

        
        self.display.fill(pygame.Color(0,0,0,1))

        self.display.blit(self.bg, (0, 0))
        
        for i in self._gameObjects:
            self.display.blit(i.image, (i.x, i.y))

        pygame.display.update()
        self.fpsClock.tick(self.FPS)

class Application(object):
    def __init__(self):
        self._state = None
        self.states = {}

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

    def addState(self, state, name):
        self.states[name] = state
        
    def start(self):
        while True:
            self.state.handleEvents()
            self.state.updateState()
            self.state.drawScreen()
