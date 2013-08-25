import pygame
from pygame.locals import *

class State(object):
    def __init__(self, owner):
        self._owner = owner
        self.background  = None

    @property
    def owner(self):
        """Application - owner of the state"""
        return self._owner

    def setBackground(self, path):
        self.background = pygame.image.load(path)
        
    def handleEvents(self):
        raise NotImplementedError("handleEvents method not implemented")

    def updateState(self):
        raise NotImplementedError("updateState method not implemented")

    def drawScreen(self):
        raise NotImplementedError("drawScreen method not implemented")

class InGame(State):

    def __init__(self, owner):
        super(InGame, self).__init__(owner)
        self._gameObjects = []
        
        pygame.mixer.init()
       
    def addGameObject(self, gameObject):
        self._gameObjects.append(gameObject)

    def handleEvent(self, event):
        raise NotImplementedError("Should have implemented this function")

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.owner.exitGame()
            self.handleEvent(event)

    def updateState(self):
        for i in self._gameObjects:
            i.updateState()

    def drawScreen(self):
        self.owner.display.fill(pygame.Color(0,0,0,1))

        self.owner.display.blit(self.background, (0, 0))
        
        for i in self._gameObjects:
            self.owner.display.blit(i.image, (i.x, i.y))
            
class MainMenu(State):
    class GuiElement(object):
        def __init__(self, owner):
            self._owner = owner

        @property
        def owner(self):
            """State - owner of GUI element"""
            return self._owner
        
        def __call__(self, event):
            raise NotImplementedError("All GUI elements must specify __call__ method")
        
    class MenuButton(GuiElement):
        def __init__(self, owner, text, action):
            super(MenuButton, self).__init__(owner)
            self._text = text
            self._action = action

        def __call__(self, event):
            if pygame.key.get() == K_ENTER:
                return self._action()

    class BarGauge(GuiElement):
        def __init__(self, owner):
            super(BarGauge, self).__init__(owner)
        def __call__(self, event):
            pass

    class SubMenu(object):
        def __init__(self, caption):
            #up to 8 fancy items!
            self._caption = caption
            self._menuItems = []
            self._position = 0
            self._selector = None

        @property
        def caption(self):
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
            self._menuItems.append(MenuItem(text, action))
    
        def handleEvents(self):
            for event in pygame.event.get([pygame.KEYDOWN]):
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
                    
    def __init__(self, owner):
        super(Paused, self).__init__(owner)
        self._menus = []
        self._currentMenu = None

    def addMenu(self, caption, item_action_dict):
        new_menu = SubMenu(caption)
        for entry, action in item_action_dict:
            new_menu.addMenuItem(entry, action)
        self._menus.append(new_menu)

   def setCurrentMenu(self, caption):
        self._currentMenu = filter(lambda m: m.caption == caption,
                                   self._menus)
                    
                


    
