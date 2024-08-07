# import pygame library
import pygame

# initialize pygame
pygame.init()

# set up the program display window - can be a list or tuple
screen = pygame.display.set_mode([800, 800])

# set title fore pygame window
pygame.display.set_caption('Misile Math')

# run until user asks to quit
running = True

# start game loop to control when game ends.
while running:

    # start the event handler code to handle all user interactions (events)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # fill background with white - list or tuple
    screen.fill((255, 255, 255))

    # draw a solid blue circle in the center
    # (which scrren to draw circle on, color, co-ordinates, radius)
    pygame.draw.circle(screen, (0, 0, 255), (400, 400), 75)

    # flip the display - updates the entire screen with everything 
    # that’s been drawn since the last flip
    pygame.display.flip()

# quit game
pygame.quit()