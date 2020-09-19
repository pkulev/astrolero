"""In-game state where all that shooting happends."""

import os
import pathlib
import random

import pygame

from eaf.core import Vec3
from eaf.state import State

from astrolero.game_entities import (
    Asteroid,
    Background,
    PlayerShip,
    WBasicLaser,
)


# TODO: Refactor this and path usage
ROOT = pathlib.Path(os.path.dirname(__file__))


class IngameState(State):

    def postinit(self):
        self.reset()

    def reset(self):
        self.background = str(ROOT / "res" / "gfx" / "space.jpg")
        self.add(self.background)

        # playership
        self.actor = PlayerShip(Vec3())
        # self.actor.x = self.app.renderer.get_width() / 2 - self.actor.width / 2
        # self.actor.y = self.app.renderer.get_height() - self.actor.height

        # self.actor.weapon = WBasicLaser(self.actor)

        self.add(self.actor)
        # test asteroidoids
        # for a in [Asteroid(self) for i in range(15)]:
        #     a.image = str(
        #         ROOT / "res" / "gfx" / "asteroids" /
        #         f"asteroid{random.randint(0, 3)}.png"
        #     )

        #     # WOW. Looks dangerous
        #     # TODO: convinient scaling for random asteroid sizing
        #     a._image = pygame.transform.scale(
        #         a.image,
        #         (a.width // random.randrange(8, 12),
        #          a.height // random.randrange(8, 12)))

        #     a.leap(random.randrange(self.app.renderer.get_width() - 300) + 150,
        #            random.randrange(self.app.renderer.get_height() - 300) + 150)
        #     a.rotateUntilStop(
        #         self.app.renderer.get_width() / 2, self.app.renderer.get_height() / 2,
        #         0.05 + random.randrange(20) / 1000.0, 100, -0.0001)
        #     self.add(a)

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, path):
        self._background = Background(path)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.stop()
            self.handleEvent(event)
