# import pygame
import pygame

#initialize pygame
pygame.init()

CIRCLE_BACKGROUND = (80, 100, 200)
CIRCLE_X = 50
CIRCLE_Y = 50
RADIUS = 20

# setup game screen
screen = pygame.display.set_mode([500, 500])

# ste screen title
pygame.display.set_caption("Move Circle")

# set up game loop
running = True

while running:

    # time delay to control the speed of the game.
    pygame.time.delay(20)

    # process user inputs
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
                running = False
        
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False


    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_LEFT]:
        CIRCLE_X -= 5

    elif keys_pressed[pygame.K_RIGHT]:
        CIRCLE_X += 5

    elif keys_pressed[pygame.K_UP]:
        CIRCLE_Y -= 5

    elif keys_pressed[pygame.K_DOWN]:
        CIRCLE_Y += 5

    # if center of the circle is less than the radius
    if CIRCLE_X < 20:
        CIRCLE_X = 20

    if CIRCLE_X > (500 - 20):
        CIRCLE_X = 490

    if CIRCLE_Y < 20:
        CIRCLE_Y = 20

    if CIRCLE_Y > 20:
        CIRCLE_Y = 20

    # fill screen background
    screen.fill( (150, 200, 215) )

    # draw circle on screen and reassign to global variable circle
    # creating a circle also returns a RECT
    pygame.draw.circle(
        screen,
        CIRCLE_BACKGROUND,
        (CIRCLE_X, CIRCLE_Y),
        RADIUS
    )

    # update game window with new objects states
    pygame.display.flip()

pygame.quit()