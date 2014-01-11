import pygame, sys

class Spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except (pygame.error, message):
            print ('Unable to load spritesheet image:', filename)
            raise (SystemExit, message)
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

if __name__ == '__main__':
    pygame.init()

    size = width, height = 240, 240
    screen = pygame.display.set_mode(size)
    komati = Spritesheet("komati.png")
    komati_imgs = [komati.image_at(r) for r in [pygame.Rect(x1, 0, x2-x1, 215) for (x1, x2) in [ (0, 105),
                                                                                                (106, 191),
                                                                                                (192, 284),
                                                                                                (285, 395),
                                                                                                (396, 496),
                                                                                                (497, 684),
                                                                                                (685, 900),
                                                                                                (901, 1111),
                                                                                                (1112, 1231),
                                                                                                (1232, 1348),
                                                                                                (1349, 1460),
                                                                                                (1461, 1562),
                                                                                                (1563, 1663),
                                                                                                (1664, 1763),
                                                                                                (1764, 1851),
                                                                                                (1852, 1955)]]]
    c = 0
    
    while 1:
        c = 0 if c == 15 else c + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill(pygame.Color(47, 95, 115, 255))
        imgRect = pygame.Rect(0, 0, 105, 215)
        imgRect.topleft = (10,10)
        screen.blit(komati_imgs[c], imgRect)
        pygame.display.flip()
        pygame.time.wait(80)
