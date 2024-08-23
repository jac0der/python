import pygame

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)

# Setup for sounds. Defaults are good.
pygame.mixer.init()

# Load all sound files
# Sound sources: Jon Fincher
move_up_sound = pygame.mixer.Sound("./assets/Rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("./assets/Falling_putter.ogg")

# Define a Character object by extending pygame.sprite.Sprite
# Instead of a surface, use an image for a better-looking sprite
class Character(pygame.sprite.Sprite):
    
    def __init__(self):

       # self.surface = pygame.Surface( (50, 50) )
       # self.surface.fill( (0, 0, 0) )

       '''
            pygame.image.load() loads an image from the disk. 
            You pass it a path to the file. It returns a Surface, 
            and the .convert() call optimizes the Surface, making 
            future .blit() calls faster.
            RLEACCEL - removes white background, make sprite thave transparency around it.
       '''
       self.surface = pygame.image.load("./assets/jet.png").convert()
       self.surface.set_colorkey((255, 255, 255), RLEACCEL)
       self.rect = self.surface.get_rect()

    # Move the Player object based on user keypresses
    def update(self, pressed_keys, screen_width, screen_height):

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            move_up_sound.play()

        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            move_down_sound.play()


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