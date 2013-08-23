#! /usr/bin/env python
from src.game import CGame, Application
from src.Classes import *
from src.Controller import *

class SGame(CGame):
    def __init__(self):
        super(SGame, self).__init__("Space Game")
        
        self.setBackground('res/space.jpg')
        
        #playership
        playerShip = PlayerShip(0,0)
        playerShip.image = 'res/Ship1.png'
        playerShip.x = self.display.get_width() / 2 - playerShip.width / 2
        playerShip.y = self.display.get_height() - playerShip.height
        playerShip.constraints.x = self.display.get_width()
        playerShip.constraints.y = self.display.get_height()

        self.addGameObject(playerShip)

        pygame.mixer.music.load('res/runaway.ogg')
        pygame.mixer.music.play(-1, 0.0)


    def handleEvent(self, event):
        pass

if __name__ == "__main__":
    App = Application()
    App.addState(SGame(), "game")
    App.state = "game"
    App.start()
