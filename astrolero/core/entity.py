from eaf.render import Renderable


class Entity(Renderable):
    """Base class for all in-game objects."""

    def __init__(self, pos, image):
        super().__init__(pos)

        import pygame
        self._image = pygame.image.load(image)

    def update(self, dt):
        pass
