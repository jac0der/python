#import pygame
import pygame

import character.character as c

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
pygame.display.set_caption("Using Sprite")

character = c.Character()

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

    # get dictonary of input keys where each key has a value of True or False. 
    # Where True is pressed and Fasle is not pressed.
    keys_pressed = pygame.key.get_pressed()

    character.update(keys_pressed, SCREEN_WIDTH, SCREEN_HEIGHT)

    # fill screen
    screen.fill( (124, 189, 215) )

    # blit player to screen at current location of the rectangle surface
    screen.blit(character.surface, character.rect) 

    pygame.display.flip()

pygame.quit()