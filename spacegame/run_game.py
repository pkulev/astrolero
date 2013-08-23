#-*- encoding: utf-8 -*-
#! /usr/bin/env python
from src.game import CGame, Application
from src.Classes import *

class SGame(CGame):
    def __init__(self, owner):
        super(SGame, self).__init__(owner)
        
        self.setBackground('res/space.jpg')
        
        #playership
        playerShip = PlayerShip(0,0)
        playerShip.image = 'res/Ship1.png'
        playerShip.x = self.owner.display.get_width() / 2 - playerShip.width / 2
        playerShip.y = self.owner.display.get_height() - playerShip.height
        playerShip.constraints.x = self.owner.display.get_width()
        playerShip.constraints.y = self.owner.display.get_height()

        self.addGameObject(playerShip)

        pygame.mixer.music.load('res/runaway.ogg')
        pygame.mixer.music.play(-1, 0.0)


    def handleEvent(self, event):
        pass

if __name__ == "__main__":
    App = Application("PYГAME: CTAДNЯ")
    App.addState(SGame, "game")
    App.state = "game"
    App.start()
