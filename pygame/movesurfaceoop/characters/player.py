import pygame
# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)

# create a class for a player, which is created as a surface.
class Player():
    
    def __init__(self):

        self.surface = pygame.Surface( (50, 50) )
        self.surface.fill( (255, 255, 255) )
        self.rect = self.surface.get_rect()

    # Move the Player object based on user keypresses
    def update(self, pressed_keys, screen_width, screen_height):

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)

        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)

        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > screen_width:
            self.rect.right = screen_width

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height