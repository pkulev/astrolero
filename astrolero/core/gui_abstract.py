import pygame

from eaf.render import Renderable


class GuiElement(Renderable):
    def __init__(self):
        super().__init__()

        self._font = None

    @property
    def font(self):
        """Current font. You can specify it's size"""
        return self._font
         
    @font.setter
    def font(self, size):
        self._font = pygame.font.Font(None, size)

    # TODO:
    def get_render_data(self):
        pass
         
    def draw(self):
        raise NotImplementedError("All GUI element must specify draw method")
         
    def __call__(self, event):
        raise NotImplementedError("All GUI elements must specify __call__ method")
