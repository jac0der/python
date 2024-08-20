# import pygame
import pygame

# initialize pygame
pygame.init()

# define global constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

SURF_WIDTH = 50
SURF_HEIGHT = 50

# setup screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# set screen title
pygame.display.set_caption("Blit Surfaces")

# setup game loop
running = True

while running:

    # process user inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False

    # draw on the screen by filling with a color
    screen.fill((130, 100, 100))

    new_surface = pygame.Surface((SURF_WIDTH, SURF_HEIGHT))

    # fill new curface with white color
    new_surface.fill( (255,255,255) )

    # to see the new surface on the screen, I have to blit it
    # to the screen at a specified location.
    screen.blit( 
        new_surface, 
        ( ((SCREEN_WIDTH - SURF_WIDTH)/2), ((SCREEN_HEIGHT - SURF_HEIGHT)/2) ) 
    )

    pygame.display.flip()

pygame.quit()