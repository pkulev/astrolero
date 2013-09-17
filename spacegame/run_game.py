#!/usr/bin/env python
#-*- coding: utf-8 -*-
import random

from pygame.locals import *

from src.main_menu import MainMenu
from src.in_game import InGame
from src.application import Application
from src.game_entities import *


class SGame(InGame):
    def __init__(self, owner):
        super(SGame, self).__init__(owner)
        self.reset()

    def reset(self):
        self._gameObjects = []
        self.background = 'res/space.jpg'

        #playership
        playerShip = PlayerShip(self, 0, 0)
        playerShip.image = 'res/Ship1.png'
        playerShip.x = self.owner.display.get_width() / 2 - playerShip.width / 2
        playerShip.y = self.owner.display.get_height() - playerShip.height
        playerShip.constraints.width = self.owner.display.get_width()
        playerShip.constraints.height = self.owner.display.get_height()

        playerShip.currentWeapon = Weapon(playerShip, "basicCannon")
        self._playerShip = playerShip

        self.addGameObject(playerShip)
        #test asteroidoids
        asteroid = [Asteroid(self) for i in range(4)]
        for a in asteroid:
            a.image = 'res/asteroid{}.png'.format(random.randrange(1,3))
            #WOW. Looks dangerous
            #TODO: convinient scaling for random asteroid sizing
            a._image = pygame.transform.scale(a.image, (a.width // random.randrange(4,6),
                                                        a.height // random.randrange(4,6)))
            a.spawn(random.randrange(self.owner.width),
                    random.randrange(self.owner.height - 300))
            self.addGameObject(a)
            

    def updateState(self):
        dx = 5
        dy = 5
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LSHIFT]:
            dx = 2
            dy = 2

        key_action_map = {
            K_w: lambda: self.movePlayerShip(0, -dy),
            K_a: lambda: self.movePlayerShip(-dx, 0),
            K_s: lambda: self.movePlayerShip(0,  dy),
            K_d: lambda: self.movePlayerShip(dx,  0),
            K_z: lambda: self.openFire()
        }

        for k in key_action_map:
            if pressed_keys[k]:
                key_action_map[k]()

        for i in self._gameObjects:
            i.updateState()

    def handleKeydown(self, key):
        {
            K_ESCAPE: lambda: self.owner.setState("Pause")
        }.get(key, lambda: None)()

    def handleKeyup(self, key):
        pass

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            self.handleKeydown(event.key)
        elif event.type == pygame.KEYUP:
            self.handleKeyup(event.key)
        else:
            pass

    def movePlayerShip(self, dx, dy):
        self._playerShip.centerx += dx
        self._playerShip.centery += dy

    def openFire(self):
        self._playerShip.currentWeapon.fire()

class SMainMenu(MainMenu):
    def __init__(self, owner):
        super(SMainMenu, self).__init__(owner)

        self.background = 'res/mainmenu/logo.png'
        self.music = 'res/runaway.ogg'
        self.play_music()
        self.addMenu("Main Menu", [
            ("Start Game", lambda: self.setCurrentMenu("Start Game")),
            ("Highscores", lambda: self.setCurrentMenu("High Scores")),
            ("Quit", self.owner.exitGame)
        ])

        self.addMenu("Start Game", [
            ("Single player", self.switchToGameState),
            ("Two players", lambda: print("two players")),
            ("Back", lambda: self.setCurrentMenu("Main Menu"))
        ])
        
        self.addMenu("High Scores", [
            ("foo", lambda: print("foo")),
            ("Back", lambda: self.setCurrentMenu("Main Menu"))
        ])


        
        self.getMenu("Main Menu").menu_center_y = 320
        self.getMenu("Main Menu").caption_center_y = 250

        self.getMenu("Start Game").menu_center_y = 320
        self.getMenu("Start Game").caption_center_y = 250
        
        self.getMenu("High Scores").menu_center_y = 320
        self.getMenu("High Scores").caption_center_y = 250

        self.setCurrentMenu("Main Menu")

        
    def switchToGameState(self):
        self.owner.setState("game")
        self.owner.state.reset()

    def switchToPause(self):
        self.owner.setState("pauseMenu")

        
class SPause(MainMenu):
    def __init__(self, owner):
        super(SPause, self).__init__(owner)

        self.background = "res/mainmenu/logo.png"
        self.music = "res/runaway.ogg"
        self.play_music()

        self.addMenu("Pause", [
            ("Continue", lambda: self.owner.setState("game")),
            ("Main Menu", lambda: self.setCurrentMenu("Main Menu"))
            ])        
        
if __name__ == "__main__":
    random.seed("menacing llama wool spike")
    App = Application("PYГAME: CTAДNЯ")
    App.addState(SGame, "game")
    App.addState(SMainMenu, "mainMenu")
    App.addState(SPause, "pauseMenu")
    App.state = "mainMenu"
    App.start()
