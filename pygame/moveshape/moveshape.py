# import pygame
import pygame

# initialize pygame
pygame.init()

# define global constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

REC_HEIGHT = 50
REC_WIDTH = 50
REC_COLOR = (114, 180, 200)

REC_X = ((SCREEN_WIDTH-REC_WIDTH)/2)
REC_Y = ((SCREEN_WIDTH-REC_WIDTH)/2)
REC_VELOCITY = 15

BACKGROUND_COLOR = (104, 70, 110)

# setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set screen title
pygame.display.set_caption("Move Shape")

# setup game loop
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

    # get dictonary where each key has a value of True or False. 
    # Where True is pressed and Fasle is not pressed.
    keys_pressed = pygame.key.get_pressed()

    # check for key presses and set new x,y co-ordinates to draw rectangle on screen
    # at different position on each iteration of the game loop.
    if keys_pressed[pygame.K_LEFT]:
        REC_X = REC_X - REC_VELOCITY

    elif keys_pressed[pygame.K_RIGHT]:
        REC_X = REC_X + REC_VELOCITY

    elif keys_pressed[pygame.K_UP]:
        REC_Y -= REC_VELOCITY

    elif keys_pressed[pygame.K_DOWN]:
        REC_Y += REC_VELOCITY

    # fill screen with white
    screen.fill(BACKGROUND_COLOR)

    # ensure rectangle doesn't go off the screen
    if REC_X < 0:
        REC_X = 0

    if REC_X  > (SCREEN_WIDTH - REC_WIDTH):
        REC_X = SCREEN_WIDTH - REC_WIDTH

    if REC_Y > (SCREEN_HEIGHT - REC_HEIGHT):
        REC_Y = (SCREEN_HEIGHT - REC_HEIGHT)
        
    if REC_Y < 0:
        REC_Y = 0

    # draw rectangle at new position on screen on each iteration of game loop.
    pygame.draw.rect(
        screen,
        REC_COLOR,
        (REC_X, REC_Y, REC_WIDTH, REC_HEIGHT)
    )

    # update game window with new objects states
    pygame.display.flip()
    # pygame.display.update() # This updates the screen so we can see my rectangle

# exit the game
pygame.quit()