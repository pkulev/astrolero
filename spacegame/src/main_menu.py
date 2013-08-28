from .core.state import State
from .core.gui import *
import pygame

class MainMenu(State):
    def __init__(self, owner):
        super(MainMenu, self).__init__(owner)
        pygame.font.init()
        self._menus = []
        self._currentMenu = None

    def addMenu(self, caption, item_action_dict):
        if caption in list(map(lambda m: m.caption,
                               self._menus)):
            raise KeyError("Menu '{0}' already exists".format(caption))
        new_menu = SubMenu(self, caption)
        print(item_action_dict)
        for entry, action in item_action_dict.items():
            print(entry)
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

    def handleEvents(self):
        if pygame.event.get([pygame.QUIT]): self.owner.exitGame()
        for event in pygame.event.get([pygame.KEYDOWN]):
            self._currentMenu.handleEvents(event)

    def updateState(self):
        pass

    def drawScreen(self):
        self.owner.display.fill(pygame.Color(0, 0, 0, 1))
        self.owner.display.blit(self.background, (0, 0))
        self._currentMenu.draw()
