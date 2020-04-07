import os
import pathlib
import random

import pygame

from eaf.state import State
from eaf.render import Renderable

from astrolero.game_entities import (
    PlayerShip,
    WBasicLaser,
    Asteroid,
)


# TODO: Refactor this and path usage
ROOT = pathlib.Path(os.path.dirname(__file__))


class IngameState(State):

    def __init__(self, app):
        super().__init__(app)
        self._background = None
        self._actor = None
        self.reset()

    @property
    def actor(self):
        return self._actor

    def reset(self):
        self.background = str(ROOT / "res" / "gfx" / "space.jpg")
        self.add(self.background)

        # playership
        self._actor = PlayerShip(self, 0, 0)
        self.actor.image = str(ROOT / "res" / "gfx" / "Ship1.png")
        # playerShip.x = self.app.display.get_width() / 2 - playerShip.width / 2
        # playerShip.y = self.owner.display.get_height() - playerShip.height
        # playerShip.constraints.width = self.owner.display.get_width()
        # playerShip.constraints.height = self.owner.display.get_height()
        self.actor.x = self.app.renderer.get_width() / 2 - self.actor.width / 2
        self.actor.y = self.app.renderer.get_height() - self.actor.height
        self.actor.constraints.width = self.app.renderer.get_width()
        self.actor.constraints.height = self.app.renderer.get_height()

        self.actor.currentWeapon = WBasicLaser(self.actor)

        self.add(self.actor)
        # test asteroidoids
        for a in [Asteroid(self) for i in range(15)]:
            a.image = str(
                ROOT / "res" / "gfx" / "asteroids" /
                f"asteroid{random.randint(0, 3)}.png"
            )

            # WOW. Looks dangerous
            # TODO: convinient scaling for random asteroid sizing
            a._image = pygame.transform.scale(
                a.image,
                (a.width // random.randrange(8, 12),
                 a.height // random.randrange(8, 12)))

            a.leap(random.randrange(self.app.renderer.get_width() - 300) + 150,
                   random.randrange(self.app.renderer.get_height() - 300) + 150)
            a.rotateUntilStop(
                self.app.renderer.get_width() / 2, self.app.renderer.get_height() / 2,
                0.05 + random.randrange(20) / 1000.0, 100, -0.0001)
            self.add(a)

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, path):
        class BG(Renderable):

            def __init__(self, surface):
                self.image = surface

            def get_render_data(self):
                pass


        self._background = BG(pygame.image.load(path))

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.stop()
            self.handleEvent(event)

    def update(self):
        for obj in self._objects:
            pass

    def render(self):
        self.app.renderer.screen.fill(pygame.Color(0, 0, 0, 1))
        self.app.renderer.screen.blit(self.background.image, (0, 0))
        for i in self._objects:
            self.app.renderer.screen.blit(i.image, (i.x, i.y))
