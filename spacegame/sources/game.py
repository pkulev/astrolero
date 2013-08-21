from .Classes import *

from . import background
from . import rmanager

class CGame(object):

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

        self.gameObjects = []
   
        #background
        self.bg = None
    
        pygame.mixer.init()
        pygame.mixer.music.load('res/coll.ogg')
        pygame.mixer.music.play(1, 1)
       
    def addGameObject(self, gameObject):
        self.gameObjects.append(gameObject)

    def setBackground(self, path):
        self.bg = pygame.image.load(path)
        
    def createWindow(self, width, height, fullscreen, depth, 
                     caption="game"):
        pygame.init()
        display = pygame.display.set_mode((width, height), fullscreen, depth)
        pygame.display.set_caption(caption)
        return display

    def quit(self):
        pygame.quit()
        sys.exit()

    def handleEvent(self, event):
        raise NotImplementedError("Should  have implemented this function")

    def handleEvents(self):
        for event in pygame.event.get():
            if (event.type == QUIT or 
            (event.type == KEYDOWN and 
             event.key == K_ESCAPE)): quit()
            self.wolo_lo()
            self.handleEvent(event)

    def updateState(self):
        for m in self.gameObjects:
            m.updateState()

    def drawScreen(self):
        self.display.fill(BLACK)

        self.display.blit(self.bg, (0, 0))
        
        for i in self.gameObjects:
            self.display.blit(i.getImage(), i.getXY())

        pygame.display.update()
        self.fpsClock.tick(self.FPS)

    def start(self):
        while True:
            self.handleEvents()
            self.updateState()
            self.drawScreen()
