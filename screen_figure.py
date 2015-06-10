import pygame

black = (0, 0, 0)
white = (255, 255, 255)

def home():
    """ Display the homepage """
    pygame.draw.rect(screen, black, (0, 0, screen.get_width(), screen.get_height()))

    rect1 = pygame.Rect(screen.get_width() / 2 - 100, 3 * screen.get_height() / 10, 200, 50)
    pygame.draw.rect(screen, white, rect1)

    rect2 = pygame.Rect(screen.get_width() / 2 - 100, 5 * screen.get_height() / 10, 200, 50)
    pygame.draw.rect(screen, white, rect2)

    font_object = pygame.font.Font(None, 50)
    font_position = (screen.get_width() / 2 - 60, 3 * screen.get_height() / 10 + 7)
    screen.blit(font_object.render("Loggin", 1, black), font_position)

    font_object = pygame.font.Font(None, 50)
    font_position = (screen.get_width() / 2 - 70, 5 * screen.get_height() / 10 + 7)
    screen.blit(font_object.render("Register", 1, black), font_position)

    pygame.display.flip()
    return rect1, rect2

def register():
    """ Display the register page  """
    pygame.draw.rect(screen, black, (0, 0, screen.get_width(), screen.get_height()))

    rect1 = pygame.Rect(screen.get_width() / 2 - 100, 3 * screen.get_height() / 10, 200, 50)
    pygame.draw.rect(screen, white, rect1)

    rect2 = pygame.Rect(screen.get_width() / 2 - 100, 5 * screen.get_height() / 10, 200, 50)
    pygame.draw.rect(screen, white, rect2)

    rect3 = pygame.Rect(screen.get_width() / 2 - 50, 7 * screen.get_height() / 10, 100, 40)
    pygame.draw.rect(screen, white, rect3)

    font_object = pygame.font.Font(None, 50)
    font_position = (screen.get_width() / 2 - 85, 3 * screen.get_height() / 10 + 7)
    screen.blit(font_object.render("Username", 1, black), font_position)

    font_object = pygame.font.Font(None, 50)
    font_position = (screen.get_width() / 2 - 80, 5 * screen.get_height() / 10 + 7)
    screen.blit(font_object.render("Password", 1, black), font_position)

    font_object = pygame.font.Font(None, 40)
    font_position = (screen.get_width() / 2 - 20, 7 * screen.get_height() / 10 + 5)
    screen.blit(font_object.render("ok", 1, black), font_position)

    pygame.display.flip()
    return rect1, rect2, rect3
    

def loggin():
    """ Display the loggin page """
    pygame.draw.rect(screen, black, (0, 0, screen.get_width(), screen.get_height()))

    rect1 = pygame.Rect(screen.get_width() / 2 - 100, 3 * screen.get_height() / 10, 200, 50)
    pygame.draw.rect(screen, white, rect1)

    rect2 = pygame.Rect(screen.get_width() / 2 - 100, 5 * screen.get_height() / 10, 200, 50)
    pygame.draw.rect(screen, white, rect2)

    rect3 = pygame.Rect(screen.get_width() / 2 - 150, 7 * screen.get_height() / 10, 300, 50)
    pygame.draw.rect(screen, white, rect3)

    font_object = pygame.font.Font(None, 50)
    font_position = (screen.get_width() / 2 - 85, 3 * screen.get_height() / 10 + 7)
    screen.blit(font_object.render("Username", 1, black), font_position)

    font_object = pygame.font.Font(None, 50)
    font_position = (screen.get_width() / 2 - 80, 5 * screen.get_height() / 10 + 7)
    screen.blit(font_object.render("Password", 1, black), font_position)

    font_object = pygame.font.Font(None, 50)
    font_position = (screen.get_width() / 2 - 110, 7 * screen.get_height() / 10 + 7)
    screen.blit(font_object.render("Go to Lobby !", 1, black), font_position)

    pygame.display.flip()
    return rect1, rect2, rect3

def lobby():
    """ Display the lobby page """
    pygame.draw.rect(screen, black, (0, 0, screen.get_width(), screen.get_height()))

    rect1 = pygame.Rect(screen.get_width() / 2 - 100, 3 * screen.get_height() / 10, 200, 50)
    pygame.draw.rect(screen, white, rect1)

    rect2 = pygame.Rect(screen.get_width() / 2 - 100, 5 * screen.get_height() / 10, 200, 50)
    pygame.draw.rect(screen, white, rect2)

    font_object = pygame.font.Font(None, 50)
    font_position = (screen.get_width() / 2 - 40, 3 * screen.get_height() / 10 + 7)
    screen.blit(font_object.render("Join", 1, black), font_position)

    font_object = pygame.font.Font(None, 50)
    font_position = (screen.get_width() / 2 - 60, 5 * screen.get_height() / 10 + 7)
    screen.blit(font_object.render("Create", 1, black), font_position)

    pygame.display.flip()
    return rect1, rect2


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Hanabi")
    screen_size = [640, 480]
    screen = pygame.display.set_mode(screen_size)
    done = False
    which_screen = 0    # 0: home; 1: register; 2: loggin; 3: lobby
    while not done:
        event_list = pygame.event.get()
        for event in event_list:
            # current page: homepage
            if which_screen == 0:
                rect1, rect2 = home()
                if event.type == pygame.QUIT:
                    done = True
                # notes: Both pygame.MOUSEBUTTONUP & pygame.MOUSEBUTTONDOWN
                #        can be used to detect mouse click; while
                #        pygame.MOUSEMOTION is in charge of motion of mouse.
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    if rect1.collidepoint(mouse_pos):
                        # TODO: loggin
                        which_screen = 2
                        print("Loggin button is pressed.")
                    elif rect2.collidepoint(mouse_pos):
                        # TODO: register
                        print("Register button is pressed.")
                        which_screen = 1
            # current page: register
            elif which_screen == 1:
                # TODO: register
                rect1, rect2, rect3 = register()
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    if rect1.collidepoint(mouse_pos):
                        # enter username
                        username = input("username: ")
                    elif rect2.collidepoint(mouse_pos):
                        # enter password
                        password = input("password: ")
                    elif rect3.collidepoint(mouse_pos):
                        # back to homepage
                        which_screen = 0
            # current page: loggin
            elif which_screen == 2:
                # TODO: loggin
                rect1, rect2, rect3 = loggin()
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    if rect1.collidepoint(mouse_pos):
                        # enter username
                        username = input("username: ")
                    elif rect2.collidepoint(mouse_pos):
                        # enter password
                        password = input("password: ")
                    elif rect3.collidepoint(mouse_pos):
                        # back to homepage
                        # TODO: check if this user exist
                        which_screen = 3
            # current page: lobby
            elif which_screen == 3:
                # TODO: lobby
                rect1, rect2 = lobby()
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()