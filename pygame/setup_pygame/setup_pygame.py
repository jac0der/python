# import pygame library
import pygame

# initialize pygame
pygame.init()

# set up the drawing window - can be a list or tuple
screen = pygame.display.set_mode([800, 800])

# run until user asks to quit
running = True

# start game loop
while running:

    # start the event handler code to handle all user interactions
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # fill background with white
    screen.fill((255, 255, 255))

    # draw a solid blue circle in the center
    # (which scrren to draw circle on, color, co-ordinates, radius)
    pygame.draw.circle(screen, (0, 0, 255), (400, 400), 75)

    # flip the display 
    pygame.display.flip()

# quit game
pygame.quit()