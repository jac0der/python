# import pygame
import pygame

# import player module which defines the player object
import characters.player as p

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

player = p.Player()

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

    # fill screen
    screen.fill( (0, 0, 0) )

    # get dictonary of input keys where each key has a value of True or False. 
    # Where True is pressed and Fasle is not pressed.
    keys_pressed = pygame.key.get_pressed()

    player.update(keys_pressed, SCREEN_WIDTH, SCREEN_HEIGHT)

    # blit player to screen at current location of the rectangle surface
    screen.blit(player.surface, player.rect) 

    # update screen with new statuses of surface object as it changes during game loop
    pygame.display.flip()

# exit the game
pygame.quit()