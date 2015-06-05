import os
import time
import socket
import select

class Judge:

    def __init__(self, jID=None,
                 room_in_charge=None,
                 game_info=None,
                 port=None,
                 IP_list=[]):

        """
        :type   jID: int
        :param  jID: ID of the judge

        :type   room_in_charge: Room object
        :param  room_in_charge: room the judge is currently in charge of

        :type   game_info:
        :param  game_info:

        :type   port: int
        :param  port: port number of the judge

        :type   IP_list: a list of user IP

        """
        self.jID = jID
        self.room_in_charge = room_in_charge
        # TODO: don't understand what game_info is ...
        self.game_info = None
        self.port = port
        self.IP_list = IP_list

    def run(self):
        print("Judge: " + str(self.jID) + " Start!")
        self.conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn_sock.bind((socket.gethostname(), self.port))
        self.conn_sock.listen(len(self.IP_list))
        self.rqueue = [self.conn_sock]

        while 1:

            rlist, wlist, elist = select.select(self.rqueue, [], [], 1)

            for s in rlist:
                csock, addr = self.conn_sock.accept()
                print("Client successfully connects!")


