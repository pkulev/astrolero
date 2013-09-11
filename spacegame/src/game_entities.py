import sys
import random

from .core.entity import *


class Ship(Entity):
    def __init__(self, owner):
        super(Ship, self).__init__(owner)
        self._currentWeapon = None

        @property
        def currentWeapon(self):
            return self._currentWeapon
        @currentWeapon.setter
        def currentWeapon(self, weapon):
            self._currentWeapon = weapon

class PlayerShip(Ship):
    def __init__(self, startX, startY, owner):
        super(PlayerShip, self).__init__(owner)
        self._x = startX
        self._y = startY
        self.baseType = "PlayerShip"

    def updateState(self):
        self.updatePosition()

    def updatePosition(self):
        pass


class EnemyShip(Ship):
    def __init__(self, startX, startY, owner):
        super(EnemyShip, self).__init__(owner)
        self.baseType = "EnemyShip"


class Weapon(Entity):
    def __init__(self, wtype, owner):
        super(Weapon, self).__init__(owner)
        self.wtype = wtype
        
    def fire(self):
        print("bang!")


class Asteroid(Entity):
    def __init__(self, owner):
        super(Asteroid, self).__init__(owner)
        self._owner = owner
#TODO: speed increasing based on level (difficulty?)
#TODO: move velocity and acceleration in physics class
        self.velocity = random.randint(1, 2)
        self.acceleration = random.randint(1, 2)

    def move(self, dt):
        self.x -= self.velocity * dt
        self.y += self.velocity * dt
        
    def spawn(self, x, y):
        self.x = x
        self.y = y

    def updateState(self):
        self.move(1)

    def handleEvents(self):
        pass
