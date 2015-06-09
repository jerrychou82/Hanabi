import pygame
from pygame.locals import *


def main():

    # initialize game
    pygame.init()

    # set up screen size and caption
    pygame.display.set_caption("Hanabi")
    screen_size = [640, 480]
    screen = pygame.display.set_mode(screen_size)

    black = (0, 0, 0)
    white = (255, 255, 255)

    # display the loggin page
    pygame.display.flip()

    # loop until the close button is clicked
    done = False
    while not done:
        for event in pygame.event.get():
            # the close button is clicked -> end the game
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEMOTION:

    # close the window and release the resource
    pygame.quit()


if __name__ == '__main__':
    main()
