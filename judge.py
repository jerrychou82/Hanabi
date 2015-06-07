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
        print("Judge: " + str(self.jID) + " Start!")
        self.conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn_sock.bind((socket.gethostname(), self.port))
        self.conn_sock.listen(len(self.IP_list))
        self.rqueue = [self.conn_sock]
        
        self.show_IP_list()

        while self.conn_num != len(self.IP_list):

            rlist, wlist, elist = select.select(self.rqueue, [], [], 1)

            for s in rlist:
                csock, addr = self.conn_sock.accept()
                print("Client successfully connects!: " + str(addr))
                self.csock_list.append(csock)
                uindex = -1
                for i in range(len(self.IP_list)):
                    if addr[0] == self.IP_list[i][0]:
                        uindex = i
                if uindex != -1:
                    self.user_status[uindex] = "CONN"
                    self.conn_num += 1
                    self.csock_list[uindex] = s

        print("Every player has connected!")
        for s in self.csock_list:
            s.send("startgame".encode('UTF-8'))
            uindex = self.csock_list.index(s)
            print("  Send startgame to: " + str(self.IP_list[uindex]))

    # show the IP list of this judge
    def show_IP_list(self):
        print("IP list of room " + str(self.room_in_charge))
        for ip in self.IP_list:
            print("  " + str(ip[0]))
