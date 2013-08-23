from pygame import K_ESCAPE, K_w, K_a, K_s, K_d

class Controller(object):
    '''Class for handle user input, changes state based keys'''
    def __init__(self, keymap = None):
        if keymap:
            self.keymap = keymap
        else:
            self.keymap = {K_ESCAPE: exitGame}

    def handleKey(self, event):
        if key in self.keymap.keys():
            return self.keymap[key]

    def handleInput(self, event):
        if event.type == "KEYUP" or event.type == "KEYDOWN":
            self.handleKey(self, event)


