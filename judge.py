import os
import time
import socket
import select
from random import shuffle
import math

class Judge:

    def __init__(self, jID=None,
                 room_in_charge=None,
                 game_info=None,
                 port=None,
                 IP_list=[]):
        
        self.jID            = jID
        self.room_in_charge = room_in_charge
        self.game_info      = None
        self.port           = port
        self.IP_list        = IP_list
        self.csock_list     = ['None']*len(IP_list)
        self.conn_num       = 0
        self.user_status    = []

        for i in range(len(IP_list)):
            self.user_status.append("UNCONN")

    # execute after init
    def run(self):
        
        # init
        self.sock_init()
        self.show_IP_list()
        while self.conn_num != len(self.IP_list):
            rlist, wlist, elist = select.select(self.rqueue, [], [], 1) 
            self.sock_handle(rlist)
        self.after_conn()

        # Start game
        self.game_init()


    # show the IP list of this judge
    def show_IP_list(self):
        print("IP list of room " + str(self.room_in_charge))
        for ip in self.IP_list:
            print("  " + str(ip[0]))

    # init sock
    def sock_init(self):
        print("Judge: " + str(self.jID) + " Start!")
        self.conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn_sock.bind((socket.gethostname(), self.port))
        self.conn_sock.listen(len(self.IP_list))
        self.rqueue = [self.conn_sock]

    # handle new coming socket
    def sock_handle(self, rlist):
        for s in rlist:
            csock, addr = self.conn_sock.accept()
            print("Client successfully connects!: " + str(addr))
            uindex = -1
            for i in range(len(self.IP_list)):
                if addr[0] == self.IP_list[i][0]:
                    uindex = i
            if uindex != -1:
                self.user_status[uindex] = "CONN"
                self.conn_num += 1
                self.csock_list[uindex] = csock

    # shuffle the desk and inform every player after all the players have been connected
    def after_conn(self):
        print("Every player has connected!")

        serve_msg = self.shuffle_and_serve()
        
        for i in range(len(self.csock_list)):
            info = "startgame " + str(i) + " " + str(self.conn_num) +  serve_msg
            self.csock_list[i].send(info.encode('UTF-8'))
            print("  Send startgame to: " + str(self.IP_list[i]))

    # init game: shuffle, distribute cards
    def game_init(self):
  
        # init Game
        print("init Game")

    # shuffle the desk and return the serving result
    def shuffle_and_serve(self):
        # shuffle
        self.desk = list(range(50))
        shuffle(self.desk)
        self.cur_card_index = 0

        # serve cards
        msg = ""
        for playeridx in range(self.conn_num):
            for i in range(4):
                cardID = self.desk[self.cur_card_index]
                card = self.cardID_to_card(cardID)
                self.cur_card_index += 1
                msg += " " + str(card[0]) + " " + str(card[1])

        return msg

    def cardID_to_card(self, cardID):
        card_color = cardID // 10
        res = cardID % 10
        if res <= 2:
            card_num = 1
        elif res <= 4:
            card_num = 2
        elif res <= 6:
            card_num = 3
        elif res <= 8:
            card_num = 4
        else:
            card_num = 5
        return (card_color, card_num)

