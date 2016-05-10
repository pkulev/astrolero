"""Example of sprite animation."""

import sys

import pygame


class Spritesheet(object):
    """Spritesheet loader."""

    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as message:
            print("Unable to load spritesheet image:", filename)
            raise Exception(message)

    def image_at(self, rectangle):
        "Load image from x,y,x+offset,y+offset"

        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        return image


def main():
    """Entry point."""

    pygame.init()

    width, height = 240, 240
    size = (width, height)
    screen = pygame.display.set_mode(size)
    komati = Spritesheet("komati.png")

    # TODO: Rewrite this shit
    komati_imgs = [
        komati.image_at(r)
        for r in [
            pygame.Rect(x1, 0, x2-x1, 215)
            for (x1, x2) in [
                (0, 105),
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
    frame = 0

    while True:
        if frame == 15:
            frame = 0
        else:
            frame += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(pygame.Color(47, 95, 115, 255))
        img_rect = pygame.Rect(0, 0, 105, 215)
        img_rect.topleft = (10, 10)
        screen.blit(komati_imgs[frame], img_rect)
        pygame.display.flip()
        pygame.time.wait(80)


if __name__ == '__main__':
    main()
