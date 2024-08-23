#import pygame
import pygame

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# define global constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# initialize pygame
pygame.init()

# setup screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# set screen title
pygame.display.set_caption("Blit Surfaces OOP")

# setup game loop
running = True

while running:

    # time delay to control the speed of the game.
    pygame.time.delay(20)

    # process user inputs
    for event in pygame.event.get():

        if event.type == QUIT:
                running = False

        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                running = Fasle

    pygame.display.flip()

pygame.quit()