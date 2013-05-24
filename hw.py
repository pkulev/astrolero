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

class Coord(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        print "({0}; {1})".format(self.x, self.y)
    
    def getXY(self):
        return (self.x, self.y)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    def setXY(self, x, y):
        self.x = x
        self.y = y

#class


class game(object):

    def __init__(self):
        self.FPS = 60
        self.fpsClock = pygame.time.Clock()
        
        pygame.init()
        self.display = pygame.display.set_mode((640, 480), 0, 32)
        pygame.display.set_caption('Animation')
        self.mycat = self.catImg = pygame.image.load('res/cat.png')
        
        self.catCoord = Coord(10, 10)
#        self.fontObj = pygame.font.Font('freesansbold.ttf', 16)
#        self.mytext = self.fontObj.render("L", True, RED)
#        self.mytextRect = self.mytext.get_rect()
#        self.mytextRect.center = (self.mycat.get_width() / 2, self.mycat.get_height() / 2)
#        self.textSurfaceObj = self.fontObj.render(self.direction, True, BLACK, WHITE)
#        self.textRectObj = self.textSurfaceObj.get_rect()
#        self.textRectObj.center = (200, 150)

        pygame.mixer.music.load('res/runaway.mp3')
        pygame.mixer.music.play(-1, 0.0)
        
        self.keyToDir = {
            273: "up",
            119: "up",
            274: "down",
            115: "down",
            275: "right",
            100: "right",
            276: "left",
            97: "left"
            }
        self.direction = None
        
    def init(self):
        pass

    def quit(self):
        pass

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key in self.keyToDir.keys():
                print "KEY {0} MOD {1}".format(event.key, event.mod)
                self.direction = self.keyToDir[event.key]
            else:
                print(event)

    def updateState(self):
        if self.direction == "up":
            self.catCoord.setY(self.catCoord.getY() - 25)
            if self.catCoord.getY() < 0:
                self.catCoord.setY(0)
            self.direction = None
        elif self.direction == "down":
            self.catCoord.setY(self.catCoord.getY() + 25)
            if self.catCoord.getY() + self.catImg.get_height() >= self.display.get_height():
                self.catCoord.setY(self.display.get_height() - self.catImg.get_height())
            self.direction = None
        elif self.direction == "right":
            self.catCoord.setX(self.catCoord.getX() + 25)
            if self.catCoord.getX() + self.catImg.get_width() >= self.display.get_width():
                self.catCoord.setX(self.display.get_width() - self.catImg.get_width())
            self.direction = None
        elif self.direction == "left":

            self.catCoord.setX(self.catCoord.getX() - 25)
            if self.catCoord.getX() <= 0:
                self.catCoord.setX(0)
            self.direction = None
        else:
            pass
        

    def drawScreen(self):
        self.display.fill(WHITE)
        self.display.blit(self.catImg, self.catCoord.getXY())
        pygame.display.update()
        self.fpsClock.tick(self.FPS)


catgame = game()

while True:
    catgame.handleEvents()
    catgame.updateState()
    catgame.drawScreen()
