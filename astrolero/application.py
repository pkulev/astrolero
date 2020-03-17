import sys

import pygame

from eaf.app import Application
from eaf.render import Renderer


class PygameRenderer(Renderer):

    def clear(self):
        pass

    def render_objects(self, objects):
        pass

    def present(self):
        pass


class PygameApplication(Application):
    def __init__(self, resolution=(0, 0), flags=0, depth=0):
        window = pygame.display.set_mode(resolution, flags, depth)
        renderer = PygameRenderer(window)

        super().__init__(renderer)

        pygame.key.set_repeat(50, 50)

    def set_caption(self, caption: str, icontitle: str = ""):
        """Set window caption.

        :param caption: window caption
        :param icontitle: short title
        """

        pygame.display.set_caption(caption, icontitle)

    def stop(self):
        self._ioloop.add_callback(pygame.quit)
        super().stop()
