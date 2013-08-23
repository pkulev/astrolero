import os, sys
from random import randint, choice
from math import sin, cos, radians

import pygame
from pygame.sprite import Sprite

from vec2d import vec2d


class Creep(Sprite):
    """ A creep sprite that bounces off walls and changes its
        direction from time to time.
    """
    def __init__(   
            self, screen, img_filename, init_position, 
            init_direction, speed):
        """ Create a new Creep.
        
            screen: 
                The screen on which the creep lives (must be a 
                pygame Surface object, such as pygame.display)
            
            img_filaneme: 
                Image file for the creep.
            
            init_position:
                A vec2d or a pair specifying the initial position
                of the creep on the screen.
            
            init_direction:
                A vec2d or a pair specifying the initial direction
                of the creep. Must have an angle that is a 
                multiple of 45 degres.
            
            speed: 
                Creep speed, in pixels/millisecond (px/ms)
        """
        Sprite.__init__(self)
        
        self.screen = screen
        self.speed = speed
        
        # base_image holds the original image, positioned to
        # angle 0.
        # image will be rotated.
        #
        self.base_image = pygame.image.load(img_filename).convert_alpha()
        self.image = self.base_image
        
        # A vector specifying the creep's position on the screen
        #
        self.pos = vec2d(init_position)

        # The direction is a normalized vector
        #
        self.direction = vec2d(init_direction).normalized()
            
    def update(self, time_passed):
        """ Update the creep.
        
            time_passed:
                The time passed (in ms) since the previous update.
        """
        # Maybe it's time to change the direction ?
        #
        self._change_direction(time_passed)
        
        # Make the creep point in the correct direction.
        # Since our direction vector is in screen coordinates 
        # (i.e. right bottom is 1, 1), and rotate() rotates 
        # counter-clockwise, the angle must be inverted to 
        # work correctly.
        #
        self.image = pygame.transform.rotate(
            self.base_image, -self.direction.angle)
        
        # Compute and apply the displacement to the position 
        # vector. The displacement is a vector, having the angle
        # of self.direction (which is normalized to not affect
        # the magnitude of the displacement)
        #
        displacement = vec2d(    
            self.direction.x * self.speed * time_passed,
            self.direction.y * self.speed * time_passed)
        
        self.pos += displacement
        
        # When the image is rotated, its size is changed.
        # We must take the size into account for detecting 
        # collisions with the walls.
        #
        self.image_w, self.image_h = self.image.get_size()
        bounds_rect = self.screen.get_rect().inflate(
                        -self.image_w, -self.image_h)
        
        if self.pos.x < bounds_rect.left:
            self.pos.x = bounds_rect.left
            self.direction.x *= -1
        elif self.pos.x > bounds_rect.right:
            self.pos.x = bounds_rect.right
            self.direction.x *= -1
        elif self.pos.y < bounds_rect.top:
            self.pos.y = bounds_rect.top
            self.direction.y *= -1
        elif self.pos.y > bounds_rect.bottom:
            self.pos.y = bounds_rect.bottom
            self.direction.y *= -1
    
    def blitme(self):
        """ Blit the creep onto the screen that was provided in
            the constructor.
        """
        # The creep image is placed at self.pos.
        # To allow for smooth movement even when the creep rotates
        # and the image size changes, its placement is always
        # centered.
        #
        draw_pos = self.image.get_rect().move(
            self.pos.x - self.image_w / 2, 
            self.pos.y - self.image_h / 2)
        self.screen.blit(self.image, draw_pos)
           
    #------------------ PRIVATE PARTS ------------------#
    
    _counter = 0
    
    def _change_direction(self, time_passed):
        """ Turn by 45 degrees in a random direction once per
            0.4 to 0.5 seconds.
        """
        self._counter += time_passed
        if self._counter > randint(400, 500):
            self.direction.rotate(45 * randint(-1, 1))
            self._counter = 0
    

def run_game():
    # Game parameters
    SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
    BG_COLOR = 150, 150, 80
    CREEP_FILENAMES = [
        'bluecreep.png', 
        'pinkcreep.png', 
        'graycreep.png']
    N_CREEPS = 20

    pygame.init()
    screen = pygame.display.set_mode(
                (SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    clock = pygame.time.Clock()

    # Create N_CREEPS random creeps.
    creeps = []    
    for i in range(N_CREEPS):
        creeps.append(Creep(screen,
                            choice(CREEP_FILENAMES), 
                            (   randint(0, SCREEN_WIDTH), 
                                randint(0, SCREEN_HEIGHT)), 
                            (   choice([-1, 1]), 
                                choice([-1, 1])),
                            0.1))

    # The main game loop
    #
    while True:
        # Limit frame speed to 50 FPS
        #
        time_passed = clock.tick(50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
        
        # Redraw the background
        screen.fill(BG_COLOR)
        
        # Update and redraw all creeps
        for creep in creeps:
            creep.update(time_passed)
            creep.blitme()

        pygame.display.flip()


def exit_game():
    sys.exit()


run_game()

