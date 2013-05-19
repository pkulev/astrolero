import pygame
import sys
from pygame.locals import *

AQUA      =  (  0, 255, 255)
BLACK     =  (  0,   0,   0)
BLUE      =  (  0,   0, 255)
FUCHSIA   =  (255,   0, 255)
GRAY      =  (128, 128, 128)
GREEN     =  (  0, 128,   0)
LIME      =  (  0, 255,   0)
MAROON    =  (128,   0,   0)
NAVYBLUE  =  (  0,   0, 128)
OLIVE     =  (128, 128,   0)
PURPLE    =  (128,   0, 128)
RED       =  (255,   0,   0)
SILVER    =  (192, 192, 192)
TEAL      =  (  0, 128, 128)
WHITE     =  (255, 255, 255)
YELLOW    =  (255, 255,   0)

class game(object):

    def __init__(self):
        self.FPS = 60
        self.fpsClock = pygame.time.Clock()
        
        pygame.init()
        self.display = pygame.display.set_mode((400, 300), 0, 32)
        pygame.display.set_caption('Animation')
        self.mycat = self.catImg = pygame.image.load('res/cat.png')
        
        self.catx = 10
        self.caty = 10
        self.direction = 'right'
        self.fontObj = pygame.font.Font('freesansbold.ttf', 16)
        self.mytext = self.fontObj.render("L", True, RED)
        self.mytextRect = self.mytext.get_rect()
        self.mytextRect.center = (self.mycat.get_width() / 2, self.mycat.get_height() / 2)
        self.textSurfaceObj = self.fontObj.render(self.direction, True, BLACK, WHITE)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (200, 150)

        self.soundObj = pygame.mixer.Sound('res/beeps.wav')
        self.soundObj.play()
        pygame.mixer.music.load('res/runaway.mp3')
        pygame.mixer.music.play(-1, 0.0)
        
    def init(self):
        pass

    def quit(self):
        pass
    def setText(self,string):
        self.mytext = self.fontObj.render(str(id(self.catImg) == id(self.mycat)),True,BLACK)#string, True, textSurfaceObj  BLACK, WHITE)

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            else:
                print(event)


    def updateState(self):
        if self.direction == 'right':
            self.catx += 5
            if self.catx == 280:
                self.direction = 'down'
                self.soundObj.stop()
        elif self.direction == 'down':
            self.caty += 5
            if self.caty == 220:
                self.direction = 'left'
                self.soundObj.play()
        elif self.direction == 'left':
            self.catx -= 5
            if self.catx == 10:
                self.direction = 'up'
                self.soundObj.stop()
        elif self.direction == 'up':
            self.caty -= 5
            if self.caty == 10:
                self.direction = 'right'
                self.soundObj.play()
            

    def drawScreen(self):
        self.display.fill(WHITE)
        self.setText(self.direction)
        self.catImg.blit(self.mytext, self.mytextRect)
        self.display.blit(self.mycat, ((self.display.get_width() - self.catImg.get_width()) / 2, (self.display.get_height() - self.catImg.get_height()) / 2))
        #self.display.blit(self.textSurfaceObj, self.textRectObj)
        
        self.display.blit(self.catImg, (self.catx, self.caty))
    
        pygame.display.update()
        self.fpsClock.tick(self.FPS)


catgame = game()

while True:
    catgame.handleEvents()
    catgame.updateState()
    catgame.drawScreen()
