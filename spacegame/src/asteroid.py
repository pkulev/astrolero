import random
import pygame
from .core.entity import Entity


class Asteroid(Entity):
    def __init__(self, owner):
        super(Asteroid, self).__init__(self)
        self._owner = owner
#TODO: speed increasing based on level (difficulty?)
        self.velocity = random.randint(1, 2)
        self.acceleration = random.randint(1, 2)
        self.spawnRect = pygame.Rect(0, -300, self.owner.display.get_width(),
                                     self.owner.display.get_height())

    def move(self, dt):
        self.x -= self.velocity * dt
        self.y += self.velocity * dt
        #self.velocity += self.acceleration * dt
        
    def spawn(self):
        self.x = random.randrange(0, self.spawnRect.width)
        self.y = random.randrange(0, self.spawnRect.height)

    def updateState(self):
        self.move(1)

    def handleEvents(self):
        pass
