# import and initialize pygame
import pygame
pygame.init()

# ste global variables for game window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500

# set global variables for rectangle size.
REC_HEIGHT = 50
REC_WIDTH = 50

# Define colors
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)

# setup game window
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption("Draw Shapes")


# set up game loop
running = True

while running:

    # start event handler loop to scan for any event triggered by user.
    for event in pygame.event.get():

        # check for KEYDOWN event TYPES
        if event.type == pygame.KEYDOWN:

            # end game if escape key was pressed.
            if event.key == K_ESCAPE:
                running = False

        # end game if the close button on game window was clicked
        elif event.type == pygame.QUIT:
                running = False

    # 1st way to draw on screen - by fillig game window with a color
    screen.fill(WHITE)

    # 2nd way to draw on screen - by creating shapes
    '''
        Draw green rectangles (40x40) at the four corners of the screen
    '''
    # rectangle at top left corner: x=0; y=0
    pygame.draw.rect(
        screen, 
        GREEN,
        (0, 0, 40, 40)
    )

    # rectangle at bottom left corner: x=0; y=SCREEN_HEIGHT-rec_height(40)
    # subtract the height of the rectangle from screen height
    # to make the rectangle visible on the screen.
    pygame.draw.rect(
        screen, 
        GREEN,
        (0, (SCREEN_HEIGHT - 40), 40, 40)
    )

    # rectangle at top right corner: x=SCREEN_WIDTH - rec_width(40); y=0
    # subtract the width of the rectangle from screen width
    # to make the rectangle visible on the screen.
    pygame.draw.rect(
        screen,
        GREEN,
        ((SCREEN_WIDTH - 40), 0, 40, 40)
    )

    # rectangle at top right corner: x=SCREEN_WIDTH - rec_width(40); y=0
    # subtract the width of the rectangle from screen width
    # to make the rectangle visible on the screen.
    pygame.draw.rect(
        screen,
        GREEN,
        ((SCREEN_WIDTH - 40), (SCREEN_HEIGHT - 40), 40, 40)
    )


    # update game window with new object states
    pygame.display.flip()

# exit the game
pygame.quit()