from .core.entity import *

class Weapon(Entity):
    def __init__(self):
        super(Weapon, self).__init__(self)
    
    def fire(self):
        print("bang!")


class WeaponSystem(object):
    def __init__(self):
        self._currentWeapon = None
        self._weapons = {}

    @property
    def currentWeapon(self):
        return self._currentWeapon

    @currentWeapon.setter
    def currentWeapon(self, weapon):
        self._currentWeapon = weapon

    def fire(self):
        self._currentWeapon.fire()

    def addWeapon(self, weapon, makeCurrent=True):
        self._weapons[weapon.ID, weapon)
        if makeCurrent:
            self._currentWeapon = weapon
