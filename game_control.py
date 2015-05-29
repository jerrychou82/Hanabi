"""
This module defines several classes that will be used in game system.

"""

class User:

    def __init__(self, status,
                 username, userID, userIP,
                 roomID, gameID):
        """
        :type status: string
        :param status: IDLE, ROOM, GAME, CONN

        :type username: string
        :param username: name of the user

        :type userID: int
        :param userID: ID of the user

        :type userIP: string
        :param userIP: IPv4 address of the user

        :type roomID: int
        :param roomID: ID of the room where the user in

        :type gameID: int
        :param gameID: ID of the game which the user is involved

        """
        self.status = status
        self.username = username
        self.userID = userID
        self.userIP = userIP
        self.roomID = roomID
        self.gameID = gameID


class Room:

    def __init__(self, roomID, room_status,
                 user_list, user_status):
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

    def __init__(self, judgeID,
                 room_in_charge,
                 game_info,
                 port):
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
