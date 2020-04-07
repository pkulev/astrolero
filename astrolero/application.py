import sys

import pygame

from eaf.app import Application
from eaf.render import Renderer


class PygameRenderer(Renderer):

    def __init__(self, window, fill_color=pygame.Color(0, 0, 0, 255)):
        super().__init__(window)

        self._fill_color = fill_color

    @property
    def fill_color(self):
        return self._fill_color

    @fill_color.setter
    def fill_color(self, values):
        self._fill_color = pygame.Color(*values)

    def clear(self):
        self.screen.fill(self.fill_color)

    def render_objects(self, objects):
        for obj in objects:
            self.screen.blit(obj.image, obj.pos.as_tuple2())

    def present(self):
        pass

    def get_width(self):
        return self.screen.get_width()

    def get_height(self):
        return self.screen.get_height()


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
