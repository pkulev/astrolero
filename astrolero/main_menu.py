import pygame

from pygame.locals import K_ESCAPE

from eaf.state import State

from .gui import SubMenu
from collections import OrderedDict


class MainMenu(State):
    def __init__(self, app):
        super().__init__(app)
        self._menus = []
        self._currentMenu = None
        self._background = None

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, path):
        self._background = pygame.image.load(path)

    def addMenu(self, caption, item_action_list):
        item_action_dict = OrderedDict(item_action_list)
        if caption in list(map(lambda m: m.caption,
                               self._menus)):
            raise KeyError("Menu '{0}' already exists".format(caption))
#        print(gui, SubMenu)
        new_menu = SubMenu(caption)
        for entry, action in item_action_dict.items():
            new_menu.addMenuItem(entry, action)
        self._menus.append(new_menu)

    def getMenu(self, menu_caption):
        return list(filter(lambda m: m.caption == menu_caption,
                           self._menus))[0]

    def setCurrentMenu(self, caption):
        if caption not in list(map(lambda m: m.caption,
                                   self._menus)):
            raise KeyError("Menu '{0}' does not exist".format(caption))
        self._currentMenu = list(filter(lambda m: m.caption == caption,
                                        self._menus))[0]

    def events(self):
        if pygame.event.get([pygame.QUIT]):
            self.app.stop()
        for event in pygame.event.get([pygame.KEYDOWN]):
            if event.key == K_ESCAPE:
                self.setCurrentMenu(self._menus[0].caption)
            self._currentMenu.handleEvents(event)

    def update(self):
        pass

    def render(self):
        self.app.renderer.screen.fill(pygame.Color(0, 0, 0, 1))
        self.app.renderer.screen.blit(self.background.image, (0, 0))
        self._currentMenu.draw()
