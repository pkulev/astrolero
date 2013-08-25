import pygame
from . import state

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
