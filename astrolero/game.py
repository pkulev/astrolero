import os
import random

from pygame.locals import *
import pygame

from astrolero.main_menu import MainMenu
from astrolero.in_game import IngameState
from astrolero.game_entities import *
from astrolero.levels import AsteroidBeltLevel


# TODO: Refactor this and path usage
ROOT = os.path.dirname(__file__) + "/"

pygame.display.init()
pygame.mixer.init()
pygame.font.init()


class Game(IngameState):
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
            K_z: self.openFire,
        }

        for k in key_action_map:
            if pressed_keys[k]:
                key_action_map[k]()

        for i in self._gameObjects:
            i.updateState()

    def handleKeydown(self, key):
        def to_pause_menu():
            self.app.state = "SPause"

        {
            K_ESCAPE: to_pause_menu,
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
    def __init__(self, app):
        super().__init__(app)

        self.background = ROOT + 'res/gfx/menu/logo.png'
        self.music = ROOT + 'res/snd/runaway.ogg'
        # TODO:
        # self.play_music()
        self.addMenu("Main Menu", [
            ("Start Game", lambda: self.setCurrentMenu("Start Game")),
            ("Highscores", lambda: self.setCurrentMenu("High Scores")),
            ("Quit", self.app.stop)
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
        self.app.state = "Game"
        self.app.state.reset()

    def switchToPause(self):
        self.app.state = "SPauseMenu"


class SPause(MainMenu):
    def __init__(self, app):
        super(SPause, self).__init__(app)

        self.background = ROOT + "res/gfx/menu/logo.png"
        self.music = ROOT + "res/snd/runaway.ogg"
        # TODO:
        # self.play_music()

        self.addMenu("Pause", [
            ("Continue", lambda: self.app.setState("game")),
            ("Main Menu", lambda: self.setCurrentMenu("Main Menu"))
            ])

#        self.getMenu("Continue").menu_center_y = 320
#        self.getMenu("Continue").caption_center_y = 250

#        self.getMenu("Main Menu").menu_center_y = 320
#        self.getMenu("Main Menu").caption_center_y = 250

        self.setCurrentMenu("Pause")
