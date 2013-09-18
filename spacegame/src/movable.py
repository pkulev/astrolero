from .core.entity import Entity
from math import sqrt
import time


def coroutine(function):
    def _coroutine(*args, **kwargs):
        g = function(*args, **kwargs)
        return lambda: next(g)
    _coroutine.__name__ = function.__name__
    _coroutine.__doc__ = function.__doc__
    return _coroutine

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

    @coroutine
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
        yield

    def moveUntilStop(self, dx, dy, lapse, dvx=0, dvy=0):
        '''Move in straight line until speed becomes zero
           or time reachs it's limit, whatever comes first
        '''
        self._move = self._moveUntilStop(dx, dy, lapse, dvx, dvy)

    @coroutine
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
        yield

    def rotateStraight(self, x, y, w, lapse, dw=0):
        '''Rotate about (x, y) with speed w and acceleration dw
           for lapse seconds.
        '''
        self._rotate = self._rotateStraight(x, y, w, lapse, dw)

    @coroutine
    def _rotateStraight(self, x, y, w, lapse, dw):
        current_time = time.time()
        finish_time = current_time + lapse
        while current_time < finish_time:
            rx = x - self._x
            ry = y - self._y
            r = sqrt(rx ** 2 + ry ** 2)
            v = r * w
            dx = ry / r * v
            dy = rx / r * v
            self._x += dx
            self._y -= dy
            w += dw
            current_time = time.time()
            yield
        self._rotate = None
        yield

    def updateState(self):
        if self._move:
            self._move()
        if self._rotate:
            self._rotate()
