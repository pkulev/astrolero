import pygame
from pygame.locals import *

class GuiElement(object):
    def __init__(self, owner):
        self._owner = owner

    @property
    def owner(self):
        """State - owner of GUI element"""
        return self._owner

    def draw(self):
        raise NotImplementedError("All GUI element must specify draw method")

    def __call__(self, event):
        raise NotImplementedError("All GUI elements must specify __call__ method")

class MenuButton(GuiElement):
    def __init__(self, owner, text, action):
        super(MenuButton, self).__init__(owner)
        self._text = text
        self._action = action

    def __call__(self, event):
        if event.key == K_RETURN:
            return self._action()

    def draw(self):
        pass

class BarGauge(GuiElement):
    def __init__(self, owner):
        super(BarGauge, self).__init__(owner)

    def __call__(self, event):
        pass

    def draw(self):
       pass

class SubMenu(object):
    def __init__(self, owner, caption):
        self.owner = owner
        #up to 8 fancy items!
        self._caption = caption
        self._menuItems = []
        self._position = 0
        self._selector = None

    @property
    def caption(self):
        """Menu caption"""
        return self._caption

    @property
    def selector(self):
        """Cursor image"""
        return self._selector
    @selector.setter
    def selector(self, path):
        self._selector = pygame.image.load(path)

    def addMenuItem(self, text, action):
        if len(self._menuItems) >= 8:
            raise IndexError("Too many menu items")
        self._menuItems.append(MenuButton(self, text, action))

    def handleEvents(self, event):
        if event.key == K_DOWN:
            self._position += 1
            if self._position > len(self._menuItems):
                self._position = 0
        elif event.key == K_UP:
            self._position -= 1
            if self._position < 0:
                self._position = len(self._menuItems)
        else:
            for m in self._menuItems:
                m(event)

    def draw(self):
        font = pygame.font.Font(None, 36)
        text = font.render(self._caption, 1, (0, 0, 0, 1))
        text.get_rect().centerx = self.owner.owner.width / 2
        text.get_rect().centery = 20

        for i in self._menuItems:
            i.draw()
