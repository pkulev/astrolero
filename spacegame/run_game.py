#-*- coding: utf-8 -*-
#! /usr/bin/env python
from src.core.state import InGame, MainMenu
from src.core.application import Application
from src.game_entities import *
from pygame.locals import *

class SGame(InGame):
    def __init__(self, owner):
        super(SGame, self).__init__(owner)
        
        self.background = 'res/space.jpg'
        
        #playership
        playerShip = PlayerShip(0,0)
        playerShip.image = 'res/Ship1.png'
        playerShip.x = self.owner.display.get_width() / 2 - playerShip.width / 2
        playerShip.y = self.owner.display.get_height() - playerShip.height
        playerShip.constraints.x = self.owner.display.get_width()
        playerShip.constraints.y = self.owner.display.get_height()

        self.addGameObject(playerShip)
        
    def handleKeydown(self, key):
        {K_ESCAPE: self.owner.exitGame,
         K_w: lambda: self.movePlayerShip(5, 5),
         K_a: lambda: self.movePlayerShip(5. -5),
         K_s: lambda: self.movePlayerShip(-5, 5),
         K_d: lambda: self.movePlayerShip(5, -5)
        }.get(key, lambda: None)()

    def handleKeyup(self, key):
        pass        

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            self.handleKeydown(event.key)
        elif event.type == pygame.KEYUP:
            self.handleKeyup(event.key)
        else: pass
          
    def movePlayerShip(self, dx, dy):
        print("moved")

class SMainMenu(MainMenu):
    def __init__(self, owner):
        super(SMainMenu, self).__init__(owner)

        self.background = 'res/mainmenu/logo.png'
        self.music = 'res/runaway.ogg'
        self.music.play(-1, 0.0)
        
        self.addMenu("Hello, Menu!",
                     {"Wololo": lambda: None})
        self.setCurrentMenu("Hello, Menu!")


if __name__ == "__main__":
    App = Application("PYГAME: CTAДNЯ")
    App.addState(SGame, "game")
    App.addState(SMainMenu, "mainMenu")
    
    
    App.state = "mainMenu"
    App.start()
