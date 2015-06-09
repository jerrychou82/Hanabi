import pygame
import pygame.font, pygame.event, pygame.draw
from pygame.locals import *


def home():
    """ Display the homepage """
    box_color = (255, 255, 255)
    box_position = (screen.get_width() / 2 - 100, 3 * screen.get_height() / 10, 200, 50)
    pygame.draw.rect(screen, box_color, box_position)

    box_color = (255, 255, 255)
    box_position = (screen.get_width() / 2 - 100, 5 * screen.get_height() / 10, 200, 50)
    pygame.draw.rect(screen, box_color, box_position)

    font_object = pygame.font.Font(None, 65)
    font_color = (0, 0, 0)
    font_position = (screen.get_width() / 2 - 75, 3 * screen.get_height() / 10)
    screen.blit(font_object.render("Loggin", 1, font_color), font_position)

    font_object = pygame.font.Font(None, 65)
    font_color = (0, 0, 0)
    font_position = (screen.get_width() / 2 - 88, 5 * screen.get_height() / 10)
    screen.blit(font_object.render("Register", 1, font_color), font_position)

    pygame.display.flip()

def register():
    """ Display the register page  """
    box_color = (255, 255, 255)
    box_position = (screen.get_width() / 2 - 100, 2 * screen.get_height() / 10, 200, 40)
    pygame.draw.rect(screen, box_color, box_position)

    box_color = (255, 255, 255)
    box_position = (screen.get_width() / 2 - 100, 4 * screen.get_height() / 10, 200, 40)
    pygame.draw.rect(screen, box_color, box_position)

    box_color = (255, 255, 255)
    box_position = (screen.get_width() / 2 - 100, 6 * screen.get_height() / 10, 200, 40)
    pygame.draw.rect(screen, box_color, box_position)

    box_color = (255, 255, 255)
    box_position = (screen.get_width() / 2 - 50, 8 * screen.get_height() / 10, 100, 20)
    pygame.draw.rect(screen, box_color, box_position)

    font_object = pygame.font.Font(None, 30)
    font_color = (0, 0, 0)
    font_position = (screen.get_width() / 2 - 75, 2 * screen.get_height() / 10)
    screen.blit(font_object.render("username: ", 1, font_color), font_position)

    font_object = pygame.font.Font(None, 30)
    font_color = (0, 0, 0)
    font_position = (screen.get_width() / 2 - 75, 4 * screen.get_height() / 10)
    screen.blit(font_object.render("password: ", 1, font_color), font_position)

    font_object = pygame.font.Font(None, 30)
    font_color = (0, 0, 0)
    font_position = (screen.get_width() / 2 - 75, 6 * screen.get_height() / 10)
    screen.blit(font_object.render("password again: ", 1, font_color), font_position)
    font_object = pygame.font.Font(None, 24)

    font_color = (0, 0, 0)
    font_position = (screen.get_width() / 2 - 10, 8 * screen.get_height() / 10)
    screen.blit(font_object.render("ok", 1, font_color), font_position)

    pygame.display.flip()
    

def loggin():
    """ Display the loggin page """
    box_color = (255, 255, 255)
    box_position = (screen.get_width() / 2 - 100, 2 * screen.get_height() / 10, 200, 40)
    pygame.draw.rect(screen, box_color, box_position)

    box_color = (255, 255, 255)
    box_position = (screen.get_width() / 2 - 100, 4 * screen.get_height() / 10, 200, 40)
    pygame.draw.rect(screen, box_color, box_position)

    box_color = (255, 255, 255)
    box_position = (screen.get_width() / 2 - 50, 6 * screen.get_height() / 10, 100, 20)
    pygame.draw.rect(screen, box_color, box_position)

    font_object = pygame.font.Font(None, 30)
    font_color = (0, 0, 0)
    font_position = (screen.get_width() / 2 - 75, 2 * screen.get_height() / 10)
    screen.blit(font_object.render("username: ", 1, font_color), font_position)

    font_object = pygame.font.Font(None, 30)
    font_color = (0, 0, 0)
    font_position = (screen.get_width() / 2 - 75, 4 * screen.get_height() / 10)
    screen.blit(font_object.render("password: ", 1, font_color), font_position)

    font_object = pygame.font.Font(None, 24)
    font_color = (0, 0, 0)
    font_position = (screen.get_width() / 2 - 10, 6 * screen.get_height() / 10)
    screen.blit(font_object.render("ok", 1, font_color), font_position)

    pygame.display.flip()

def lobby():
    """ Display the lobby page """
    box_color = (255, 255, 255)
    box_position = (screen.get_width() / 2 - 100, 3 * screen.get_height() / 10, 200, 30)
    pygame.draw.rect(screen, box_color, box_position)

    box_color = (255, 255, 255)
    box_position = (screen.get_width() / 2 - 100, 5 * screen.get_height() / 10, 200, 30)
    pygame.draw.rect(screen, box_color, box_position)

    font_object = pygame.font.Font(None, 30)
    font_color = (0, 0, 0)
    font_position = (screen.get_width() / 2 - 60, 3 * screen.get_height() / 10)
    screen.blit(font_object.render("Join a Room", 1, font_color), font_position)

    font_object = pygame.font.Font(None, 30)
    font_color = (0, 0, 0)
    font_position = (screen.get_width() / 2 - 60, 5 * screen.get_height() / 10)
    screen.blit(font_object.render("Create a Room", 1, font_color), font_position)

    pygame.display.flip()
    


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Hanabi")
    screen_size = [640, 480]
    screen = pygame.display.set_mode(screen_size)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # home()
        # register()
        # loggin()
        # lobby()
