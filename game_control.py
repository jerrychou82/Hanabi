"""
This module defines several classes that will be used in game system.

"""
import socket


class User:

    def __init__(self, status="CONN",
                 username=None, userID=None, userIP=None, usock=None,
                 roomID=None, gameID=None):
        """
        :type status: string
        :param status: IDLE, ROOM, GAME, CONN

        :type uname: string
        :param uname: name of the user

        :type uID: int
        :param uID: ID of the user

        :type uIP: string
        :param uIP: IPv4 address of the user

        :type usock: socket object
        :param usock: socket of the user

        :type roomID: int
        :param roomID: ID of the room where the user in

        :type gameID: int
        :param gameID: ID of the game which the user is involved

        """
        self.status = status
        self.uname = username
        self.uID = userID
        self.uIP = userIP
        self.usock = usock
        self.roomID = roomID
        self.gameID = gameID


class Room:

    def __init__(self, roomID=None, room_status=None,
                 user_list=None, user_status=None):
        """
        :type roomID: int
        :param roomID: ID of the room

        :type room_status: string
        :param room_status: WAIT, PLAY

        :type user_list: list
        :param user_list: list of User objects

        :type user_status: list (of strings)
        :param user_status: list of ths status of all users in this room

        """
        self.roomID = roomID
        self.room_status = room_status
        self.user_list = user_list
        self.user_status = user_status


class Judge:

    def __init__(self, judgeID=None,
                 room_in_charge=None,
                 game_info=None,
                 port=None):
        """
        :type judgeID: int
        :param judgeID: ID of the judge

        :type room_in_charge: Room object
        :param room_in_charge: room the judge is currently in charge of

        :type game_info:
        :param game_info:

        :type port: int
        :param port: port number of the judge

        """
        self.judgeID = judgeID
        self.room_in_charge = room_in_charge
        # TODO: don't understand what game_info is ...
        self.game_info = None
        self.port = port


def main():
    user = User(status="CONN",
                username="andyyuan", userID=16, userIP="140.112.90.192",
                roomID=1, gameID=1)


if __name__ == '__main__':
    main()
