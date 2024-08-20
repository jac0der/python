# import pygame
import pygame

#initialize pygame
pygame.init()

# define global constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

CIRCLE_BACKGROUND = (80, 100, 200)
CIRCLE_X = 50
CIRCLE_Y = 50
RADIUS = 20

VELOCITY = 5

# setup game screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

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
        CIRCLE_X -= VELOCITY

    elif keys_pressed[pygame.K_RIGHT]:
        CIRCLE_X += VELOCITY

    elif keys_pressed[pygame.K_UP]:
        CIRCLE_Y -= VELOCITY

    elif keys_pressed[pygame.K_DOWN]:
        CIRCLE_Y += VELOCITY

    #ensure circle doesnt go outside the game window.
    # if center of the circle is less than the radius
    if CIRCLE_X < RADIUS:
        CIRCLE_X = RADIUS

    if CIRCLE_Y < RADIUS:
        CIRCLE_Y = RADIUS

    # if center of the circle is greater than the r
    # # screen height minus the adius
    if CIRCLE_X > (SCREEN_WIDTH - RADIUS):
        CIRCLE_X = (SCREEN_WIDTH - RADIUS)

    if CIRCLE_Y > (SCREEN_HEIGHT - RADIUS):
        CIRCLE_Y = (SCREEN_HEIGHT - RADIUS)

    # fill screen background
    screen.fill( (150, 200, 215) )

    # draw circle on screen
    # creating a circle also returns a RECT object
    pygame.draw.circle(
        screen,
        CIRCLE_BACKGROUND,
        (CIRCLE_X, CIRCLE_Y),
        RADIUS
    )

    # update game window with new objects states
    pygame.display.flip()

# exit the game
pygame.quit()