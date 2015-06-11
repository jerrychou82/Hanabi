import os
import time
import socket
import select
import math
import game
from random import shuffle


class Judge:

    def __init__(self, jID=None,
                 room_in_charge=None,
                 game_info=None,
                 port=None,
                 IP_list=[]):
        
        self.jID                = jID
        self.room_in_charge     = room_in_charge
        self.game_info          = None
        self.port               = port
        self.IP_list            = IP_list
        self.csock_list         = ['None']*len(IP_list)
        self.conn_num           = 0
        self.user_status        = []
        self.cur_card_index     = 0
        self.cur_player_index   = 0

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

        # Game object init, suffle, and serve
        self.game_init()

        # Start game
        self.game_start()


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
    def game_init(self):

        print("Every player has connected!")

        serve_msg = self.shuffle_and_serve()
        
        for i in range(len(self.csock_list)):
            info = "startgame " + str(i) + " " + str(self.conn_num) + serve_msg[i]
            print(info)
            self.csock_list[i].send(info.encode('UTF-8'))
            print("  Send startgame to: " + str(self.IP_list[i]))
        print("After shuffle and serving!")

        # Create game object
        info = "startgame -1 " + str(self.conn_num) + serve_msg[self.conn_num]
        self.jgame = game.Game(player_num=self.conn_num, buf=info)


    def game_start(self):
        
        print("Start game!")
        time.sleep(1)

        while self.cur_card_index != 50: # while there are still cards
           
            print("Round: " + str(self.cur_card_index))
            self.jgame.show_debug()
            self.jgame.show_status()

            # send yourturn to player
            cpidx = self.cur_player_index # current player index
            self.csock_list[cpidx].send("yourturn".encode('UTF-8'))
            data = self.csock_list[cpidx].recv(4096)
            msg = data.decode('UTF-8')
            msg_list = msg.split(' ')

            if   msg_list[0] == "hit":
                cidx    = int(msg_list[1]) # card index
                ccolor  = self.jgame.players[cpidx].cards[cidx][0]
                cnumber = self.jgame.players[cpidx].cards[cidx][1]
                ncardID = self.draw_card()
                ncard   = self.cardID_to_card(ncardID)
                ncolor  = ncard[0]
                nnumber = ncard[1]
                self.jgame.hit(cpidx, cidx, self.jgame.players[cpidx].cards[cidx], ncard)
                info    = "hit " + str(cpidx) + " " + str(cidx) + " " + str(ccolor) + " " + str(cnumber)
                print("Player" + str(cpidx) + " hits card: " + str(cidx))

            elif msg_list[0] == "hint":
                hpidx   = int(msg_list[1])  # hint player index
                htype   = int(msg_list[2])  # hint type: 0: color; 1: number
                hnum    = int(msg_list[3])  # hint number
                # find cards that are hint
                hclist  = self.find_hint_card(hpidx, htype, hnum)
                hcnum   = len(hclist)       # number of cards that are hint
                self.jgame.hint(cpidx, hpidx, htype, hnum, hclist)
                info    = "hint " + str(cpidx) + " " + str(hpidx) + " " + str(htype) + " " + str(hnum) + " " + str(hcnum)
                for card in hclist:
                    info += " " + str(card)
                print("Player" + str(cpidx) + " hints player " + str(hpidx) + " on ", end="")
                if htype == "color":
                    print("color " + str(hnum))
                else:
                    print("number " + str(hnum))


            elif msg_list[0] == "throw":
                cidx    = int(msg_list[1]) # card index
                ccolor  = 0
                cnumber = 0
                ncardID = self.draw_card()
                ncard   = self.cardID_to_card(ncardID)
                ncolor  = ncard[0]
                nnumber = ncard[1]
                info    = "throw " + str(cpidx) + " " + str(cidx) + " " + str(ccolor) + " " + str(cnumber)
                print("Player" + str(cpidx) + " throws")

            # send info to everyone
            if msg_list[0] == "hit" or msg_list[0] == "throw":
                for s in self.csock_list:
                    if s == self.csock_list[cpidx]:
                        sinfo = info + " -1 -1"
                    else:
                        sinfo = info + " " + str(ncolor) + " " + str(nnumber)

                    s.send(sinfo.encode('UTF-8'))
            else:
                for s in self.csock_list:
                    s.send(info.encode('UTF-8'))

            print("  Info: " + info)

            # update next player
            self.cur_player_index = (cpidx + 1) % self.conn_num
            
            self.cur_card_index += 1

        # end of game



    # shuffle the desk and return the serving result
    def shuffle_and_serve(self):
        # shuffle
        self.desk = list(range(50))
        shuffle(self.desk)

        # serve cards
        msg = [""] * (self.conn_num+1)
        for playeridx in range(self.conn_num):
            for i in range(4):
                cardID = self.desk[self.cur_card_index]
                card = self.cardID_to_card(cardID)
                self.cur_card_index += 1
                for j in range(self.conn_num):
                    if j == playeridx:
                        msg[j] += " " + "-1" + " " + "-1"
                    else:
                        msg[j] += " " + str(card[0]) + " " + str(card[1])
                msg[self.conn_num] += " " + str(card[0]) + " " + str(card[1])

        return msg

    def draw_card(self):
        cardID = self.desk[self.cur_card_index]
        self.cur_card_index += 1
        return cardID

    def cardID_to_card(self, cardID):
        card_color = 1 + (cardID // 10)
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

    def find_hint_card(self, cpidx, htype, hnum):
        hlist = []
        for i in range(4):
            if self.jgame.players[cpidx].cards[i][htype] == hnum:
                hlist.append(i)
        return hlist

