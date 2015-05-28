#!/usr/bin/python

# -*- coding: utf-8 -*-

import pygame as pg
from pygame.locals import *

import inputbox


def main():

    # 初始化 pygame
    pg.init()

    # 設定 pygame 視窗標題 (caption)
    pg.display.set_caption("Demo")

    # 設定 pygame 視窗大小 (640 x 480)
    screen = pg.display.set_mode((640, 480))

    # 將 pygame 視窗顯示在螢幕上
    pg.display.flip()

    f = open("client_list.txt", "w")
    # 無窮迴圈
    while True:
        # 取得 pygame 的事件 (event)
        event = pg.event.wait()

        # 如果視窗的 x 被按下，就結束迴圈
        if event.type == pg.QUIT:
            break

        # Testing with inputbox.ask
        username = inputbox.ask(screen, "Enter username")
        password = inputbox.ask(screen, "Enter password")
        # print("(username, password) = (%s, %s)" % (username, password))
        new_client = username + ", " + password + "\n"
        f.write(new_client)

    f.close()

    # 釋放 pygame 的資源
    pg.quit()


if __name__ == '__main__':
    main()
