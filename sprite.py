import pygame, sys

class Spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except (pygame.error, message):
            print ('Unable to load spritesheet image:', filename)
            raise (SystemExit, message)

    def image_at(self, rectangle):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        return image

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
