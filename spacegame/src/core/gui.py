import pygame
from pygame.locals import *

class GuiElement(object):
    def __init__(self, owner):
        self._owner = owner
        self._application = owner.owner
        self._font = None

    @property
    def owner(self):
        """State - owner of GUI element"""
        return self._owner

    @property
    def application(self):
        """Master application"""
        return self._application

    @property
    def font(self):
        """Current font. You can specify it's size"""
        return self._font
    @font.setter
    def font(self, size):
        self._font = pygame.font.Font(None, size)

    def draw(self):
        raise NotImplementedError("All GUI element must specify draw method")

    def __call__(self, event):
        raise NotImplementedError("All GUI elements must specify __call__ method")

class MenuButton(GuiElement):
    def __init__(self, owner, text, action):
        super(MenuButton, self).__init__(owner)
        self._text = text
        self._action = action
        self.font = 48

    def __call__(self, event):
        if event.key == K_RETURN:
            return self._action()

    def draw(self, height):
        """Draws button centered horizontally, at the height pixels"""
        text = self._font.render(self._text, 1, (255, 255, 255, 255))
        textpos = text.get_rect()
        textpos.centerx = self.application.width / 2
        textpos.centery = height
        self.application.display.blit(text, textpos)

class BarGauge(GuiElement):
    def __init__(self, owner):
        super(BarGauge, self).__init__(owner)

    def __call__(self, event):
        pass

    def draw(self):
       pass

class SubMenu(GuiElement):
    def __init__(self, owner, caption):
        super(SubMenu, self).__init__(owner)
        #up to 8 fancy items!
        self._caption = caption
        self._caption_center_y = 20
        self._menuItems = []
        self._position = 0
        self._selector = ""
        self._menu_center_y = 100
        self._menu_item_height = 60
        self.font = 72

    def __call__(self):
        pass

    @property
    def menu_center_y(self):
        """Starting menu height. Defaults to 100 px."""
        return self._menu_center_y
    @menu_center_y.setter
    def menu_center_y(self, val):
        self._menu_center_y = val

    @property
    def item_height(self):
        """Menu item height in pixels. Default is 60"""
        return self._menu_item_height
    @item_height.setter
    def item_height(self):
        self._menu_item_height = val

    @property
    def caption_center_y(self):
        """Y position of menu caption. Default is 20"""
        return self._caption_center_y
    @caption_center_y.setter
    def caption_center_y(self, val):
        self._caption_center_y = val

    @property
    def caption(self):
        """Menu caption"""
        return self._caption

    @property
    def selector(self):
        """Cursor character"""
        return self._selector
    @selector.setter
    def selector(self, value):
        self._selector = value

    def addMenuItem(self, text, action):
        if len(self._menuItems) >= 8:
            raise IndexError("Too many menu items")
        self._menuItems.append(MenuButton(self.owner, text, action))

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
        text = self._font.render(self._caption, 1, (255, 255, 255))
        textpos = text.get_rect()
        textpos.centerx = self.application.width / 2
        textpos.centery = self._caption_center_y
        self.application.display.blit(text, textpos)

        for i,m in enumerate(self._menuItems):
            m.draw(self._menu_center_y + i * self._menu_item_height)
