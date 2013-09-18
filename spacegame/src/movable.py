from core.entity import Entity
from math import sqrt
import time


class Movable(Entity):
    def __init__(self, owner):
        super(Movable, self).__init__(owner)
        self._move = None
        self._rotate = None

    def leap(self, new_x, new_y):
        self._x = new_x
        self._y = new_y

    def moveStraight(self, dx, dy, time, dvx=0, dvy=0):
        '''Move in straight line for lapse seconds
        '''
        self._move = self._moveStraight(dx, dy, time, dvx, dvy)

    def _moveStraight(self, dx, dy, lapse, dvx, dvy):
        current_time = time.time()
        finish_time = current_time + lapse
        while current_time < finish_time:
            dx += dvx
            dy += dvy
            self._x += dx
            self._y += dy
            current_time = time.time()
            yield
        self._move = None

    def moveUntilStop(self, dx, dy, lapse, dvx=0, dvy=0):
        '''Move in straight line until speed becomes zero
           or time reachs it's limit, whatever comes first
        '''
        self._move = self._moveUntilStop(dx, dy, lapse, dvx, dvy)
        
    def _moveUntilStop(self, dx, dy, lapse, dvx, dvy):
        current_time = time.time()
        finish_time = current_time + lapse
        while dx != 0 and dy != 0 and current_time < finish_time:
            dx += dvx * it
            dy += dvy * it
            self._x += dx
            self._y += dy
            current_time = time.time()
            yield
        self._move = None
        
    def updateState(self):
        if self._move:
            next(self._move)
        if self._rotate:
            next(self._rotate)
        
        
