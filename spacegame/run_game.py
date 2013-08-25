#-*- coding: utf-8 -*-
#! /usr/bin/env python
from src.core.state import InGame
from src.core.application import Application
from src.game_entities import *
from pygame.locals import *

class SGame(InGame):
    def __init__(self, owner):
        super(SGame, self).__init__(owner)
        
        self.keydown_events = None
        self.keyup_events = None

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

    def handleKeydown(self, key):
        {K_ESCAPE: self._owner.exitGame,
         K_w: lambda: self.movePlayerShip((5,5))
        }.get(key, lambda: None)()

    def handleKeyup(self, key):
        pass        

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            self.handleKeydown(event.key)
        elif event.type == pygame.KEYUP:
            self.handleKeyup(event.key)
        else: pass
          
    def movePlayerShip(self, (dx, dy)):
        print("moved")




if __name__ == "__main__":
    App = Application("PYГAME: CTAДNЯ")
    App.addState(SGame, "game")
    App.state = "game"
    App.start()
