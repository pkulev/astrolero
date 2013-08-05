from Classes import *
import background
import CResourceManager

class Game(object):

    def __init__(self):
        self.FPS = 60
        self.fpsClock = pygame.time.Clock()
        
        pygame.init()
        self.width = 640
        self.height = 480
        self.fullscreen = 0
        self.depth = 32
        self.movables = []
        self.immovables = []
        self.keyStack = []
        
        self.display = pygame.display.set_mode((self.width, self.height), 
                                               self.fullscreen, self.depth)
        
        pygame.display.set_caption('Space game')

        RManager = CResourceManager.CResourceManager()
        #RManager.load()
        
        #background
        self.bg = background.CBackground(0,0)
        self.bg.setImage('res/space.jpg')

        self.immovables.append(self.bg)
        
        #playership
        self.playerShip = PlayerShip(0,0)
        self.playerShip.setImage('res/image 17.png')
        self.playerShip.setXY(
            self.display.get_width() / 2 - self.playerShip.get_width() / 2, 
            self.display.get_height() - self.playerShip.get_height()
            )
        self.playerShip.setConstraints(
            self.display.get_width(), 
            self.display.get_height()
            )                                         
        
        self.movables.append(self.playerShip)

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
        
    def init(self):
        pass

    def quit(self):
        pass

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESC):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and event.key in self.keyToDir.keys():
                self.keyStack.append(event.key)
                print "UP KEY {0} MOD {1} S:{2}".format(event.key, event.mod, self.keyStack)
                for m in self.movables: ## obvious crunch
                    if m.type == "PlayerShip":
                        break
                m.direction = self.keyToDir[event.key]
            elif event.type == KEYUP and event.key in self.keyToDir.keys():
                self.keyStack.pop()
                print "DOWN KEY {0} MOD {1} S:{2}".format(event.key, event.mod, self.keyStack)
                for m in self.movables: ## obvious crunch
                    if m.type == "PlayerShip":
                        break
                m.direction = None
            else:
                pass#print(event)

    def updateState(self):
        for m in self.movables:
            m.updatePosition()

    def drawScreen(self):
        self.display.fill(BLACK)

        for i in self.immovables:
            self.display.blit(i.getImage(), i.getXY())

        for m in self.movables:
                self.display.blit(m.getImage(), m.getXY())

        self.display.blit(self.bg.getImage(), self.bg.getXY())
        self.display.blit(self.playerShip.getImage(), self.playerShip.getXY())
        
        pygame.display.update()
        self.fpsClock.tick(self.FPS)
