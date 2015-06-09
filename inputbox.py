import pygame
import pygame.font, pygame.event, pygame.draw
from pygame.locals import *


def display_box(screen, message):
    """ Print a message in a box in the middle of the screen """
    font_object = pygame.font.Font(None, 18)

    box_color = (0, 0, 0)
    box_position = (screen.get_width() / 2 - 100, screen.get_height() / 2, 200, 20)  # (x, y, width, height)
    pygame.draw.rect(screen, box_color, box_position)

    outer_color = (255, 255, 255)
    outer_position = (screen.get_width() / 2 - 102, screen.get_height() / 2 - 12, 204, 24)
    pygame.draw.rect(screen, outer_color, outer_position, 1)

    assert len(message) > 0
    font_color = (255, 255, 255)
    font_position = (screen.get_width() / 2 - 100, screen.get_height() / 2 - 10)
    screen.blit(font_object.render(message, 1, font_color), font_position)

    pygame.display.flip()

def get_key():
    while True:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass

def ask(screen, message):
    pygame.font.init()
    current_string = []
    display_box(screen, message)
    while True:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == K_RETURN:
            break
        elif inkey == K_MINUS:
            current_string.append("_")
        elif inkey <= 127:
            current_string.append(chr(inkey))
        display_box(screen, message + ": ")
    return "".join(current_string)


def main():
    screen = pygame.display.set_mode((320, 240))
    print(ask(screen, "Name"))


if __name__ == '__main__':
    main()
