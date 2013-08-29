#-*- coding: utf-8 -*-
#! /usr/bin/env python
from src.main_menu import MainMenu
from src.in_game import InGame
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
        playerShip.constraints.width = self.owner.display.get_width()
        playerShip.constraints.height = self.owner.display.get_height()
        self._playerShip = playerShip

        self.addGameObject(playerShip)

    def updateState(self):
        key_action_map = {K_w: lambda: self.movePlayerShip(0, -5),
                          K_a: lambda: self.movePlayerShip(-5, 0),
                          K_s: lambda: self.movePlayerShip(0, 5),
                          K_d: lambda: self.movePlayerShip(5, 0)
                      }
        pressed_keys = pygame.key.get_pressed()
        for k in key_action_map:
            if pressed_keys[k]:
                key_action_map[k]()

        for i in self._gameObjects:
            i.updateState()

    def handleKeydown(self, key):
        {K_ESCAPE: lambda: self.owner.setState("mainMenu")
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
        self._playerShip.centerx += dx
        self._playerShip.centery += dy

class SMainMenu(MainMenu):
    def __init__(self, owner):
        super(SMainMenu, self).__init__(owner)

        self.background = 'res/mainmenu/logo.png'
        self.music = 'res/runaway.ogg'
        self.play_music()
        self.addMenu("Main Menu",
                     [("Start Game", lambda: self.owner.setState("game")),
                      ("Highscores", lambda: print("Showing HighScores!")),
                      ("Quit", self.owner.exitGame)])
        self.getMenu("Main Menu").menu_center_y = 320
        self.getMenu("Main Menu").caption_center_y = 250
        self.setCurrentMenu("Main Menu")


if __name__ == "__main__":
    App = Application("PYГAME: CTAДNЯ")
    App.addState(SGame, "game")
    App.addState(SMainMenu, "mainMenu")
    
    
    App.state = "mainMenu"
    App.start()
