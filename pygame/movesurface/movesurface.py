# import pygame
import pygame

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# initialize pygame
pygame.init()

# define global constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

SURF_WIDTH = 50
SURF_HEIGHT = 50
SURF_X = ((SCREEN_WIDTH - SURF_WIDTH)/2)
SURF_Y = ((SCREEN_HEIGHT - SURF_HEIGHT)/2)

VELOCITY = 5

# setup screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# set screen title
pygame.display.set_caption("Blit Surfaces")

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

    # check for key presses and set new x,y co-ordinates to draw new surface on screen
    # at different position on each iteration of the game loop.
    if keys_pressed[K_LEFT]:
        SURF_X -= VELOCITY

    if keys_pressed[K_RIGHT]:
        SURF_X += VELOCITY

    if keys_pressed[K_UP]:
        SURF_Y -= VELOCITY

    if keys_pressed[K_DOWN]:
        SURF_Y += VELOCITY

    # draw on the screen by filling with a color
    screen.fill((130, 100, 100))

    # create a new surface
    new_surface = pygame.Surface((SURF_WIDTH, SURF_HEIGHT))
        # fill new curface with white color (treat just as a regular surface at this point)
    new_surface.fill( (255,255,255) )

    # keep surface within the bounds of the game window
    if SURF_X < 0:        
        SURF_X = 0

    if SURF_X > (SCREEN_WIDTH - SURF_WIDTH):
        SURF_X = (SCREEN_WIDTH - SURF_WIDTH)

    if SURF_Y < 0:
        SURF_Y = 0

    if SURF_Y > (SCREEN_HEIGHT - SURF_HEIGHT):
        SURF_Y = (SCREEN_HEIGHT - SURF_HEIGHT)

    # to see the new surface on the screen, I have to blit it
    # to the screen at a specified location.
    screen.blit( 
        new_surface, 
        ( SURF_X, SURF_Y ) 
    )

    # update screen with new statuses of surface object as it changes during game loop
    pygame.display.flip()

# exit the game
pygame.quit()