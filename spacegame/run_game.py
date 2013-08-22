#! /usr/bin/env python
from sources.game import CGame
from sources.Classes import *

class SGame(CGame):
    def __init__(self):
        super(SGame, self).__init__("Space Game")
        
        self.setBackground('res/space.jpg')
        
        #playership
        playerShip = PlayerShip(0,0)
        playerShip.setImage('res/image 17.png')
        playerShip.setXY(
            self.display.get_width() / 2 - playerShip.get_width() / 2, 
            self.display.get_height() - playerShip.get_height())
        playerShip.setConstraints(
            self.display.get_width(), 
            self.display.get_height())

        self.addGameObject(self.playerShip)

    def handleEvent(self, event):
        pass

if __name__ == "__main__":
    spacegame = SGame()
    spacegame.start()
