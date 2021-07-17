"""Game entities."""

import os
import pathlib

from eaf import Vec3

from .core.entity import Entity
from .movable import Movable


# TODO: Refactor this and path usage
ROOT = pathlib.Path(os.path.dirname(__file__))


class Background(Entity):

    def __init__(self, image):
        super().__init__(Vec3(), image)



class Ship(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._weapon = None

        @property
        def weapon(self):
            return self._weapon

        @weapon.setter
        def weapon(self, obj):
            self._weapon = obj

        def move_left(self):
            self._direction = -1

        def move_right(self):
            self._direction = 1

        def move_forward(self):
            pass

        def move_backward(self):
            pass

        def fire(self):
            pass


class PlayerShip(Ship):

    def __init__(self, pos):
        super().__init__(pos, image=str(ROOT / "res" / "gfx" / "Ship1.png"))


class EnemyShip(Ship):
    pass


class Weapon(Entity):
    def __init__(self, owner):
        super(Weapon, self).__init__(owner)
        self.shell = None

    def fire(self):
        print("bang!")


class WeaponShell(Movable):
    pass

class BasicLaser(WeaponShell):
    def __init__(self, pos):
        super(BasicLaser, self).__init__(pos)
        self.leap(0, 0)
        self.rotateUntilStop(0, 0, 0, 0, 0)


class WBasicLaser(Weapon):
    def __init__(self, pos):
        super(WBasicLaser, self).__init__(pos)
        self.shell = BasicLaser

        def fire(self):
            print(self.shell())


class Asteroid(Movable):
    def __init__(self, owner):
        super(Asteroid, self).__init__(owner)

    def updateState(self):
        super(Asteroid, self).updateState()

    def handleEvents(self):
        pass
