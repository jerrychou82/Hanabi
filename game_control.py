"""
This module defines several classes that will be used in game system.

"""
import socket
import random


class User:

    def __init__(self, ustatus="CONN",
                 uname=None, uID=None, uIP=None, usock=None,
                 roomID=None, gameID=None):
        """
        :type   ustatus: string
        :param  ustatus: IDLE, ROOM, GAME, CONN

        :type   uname: string
        :param  uname: name of the user

        :type   uID: int
        :param  userID: ID of the user

        :type   uIP: string
        :param  userIP: IPv4 address of the user

        :type   usock: socket object
        :param  usock: socket of the user

        :type   roomID: int
        :param  roomID: ID of the room where the user in

        :type   gameID: int
        :param  gameID: ID of the game which the user is involved

        """
        self.ustatus = ustatus
        self.uname = uname
        self.uID = uID
        self.uIP = uIP
        self.usock = usock
        self.roomID = roomID
        self.gameID = gameID
        

    def show_user(self):
        print("Name: " + str(self.uname) + " Status: " + self.ustatus + " RoomID: " + str(self.roomID))

class Room:

    def __init__(self, rID=None, rstatus="EMPTY",
                 user_list=[], user_status=[], max_unum=4):
        """
        :type   rID: int
        :param  rID: ID of the room

        :type   rstatus: string
        :param  rstatus: EMPTY, WAIT, PLAY

        :type   user_list: list
        :param  user_list: list of User objects

        :type   user_status: list (of strings)
        :param  user_status: list of ths status of all users in this room

        :type   max_unum: int
        :param  max_unum: maximum number of users in this room

        """
        self.rID = rID
        self.rstatus = rstatus
        self.user_list = user_list
        self.user_status = user_status
        self.max_unum = max_unum
        self.user_sock = []
        self.game_time = 0

    def show_room(self):
        print("ID: " + str(self.rID) + " Status: " + self.rstatus)
        for i in range(len(self.user_list)):
            print("  " + str(self.user_list[i].uname) + " Status " + self.user_status[i])


class Unode:

    def __init__(self, uname=None, ustatus=None):
        self.uname = uname
        self.ustatus = ustatus


class Rnode:

    def  __init__(self, rID=None, max_unum=None, cur_unum=None):
        self.rID = rID
        self.max_unum = max_unum
        self.cur_unum = cur_unum


def main():
    user = User(ustatus="CONN",
                uname="andyyuan", uID=16, uIP="140.112.90.192",
                roomID=1, gameID=1)


if __name__ == '__main__':
    main()
