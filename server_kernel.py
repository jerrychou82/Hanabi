import os
import time
from game_control import *
from judge import *

class Server:
        
    # maximum number of clients
    MAX_PLAYER  = 20
    ROOM_NUM    = 10

    def __init__(self, rqueue, port_num): 
    
        # list
        self.user_list  = []
        self.room_list  = []
        self.judge_list = []
        
        # rooms init
        for i in range(Server.ROOM_NUM):
            room = Room(rID=i)
            self.room_list.append(room)
        
        # reading queue
        self.rqueue         = rqueue
        
        # port number
        self.port_num       = port_num

    # user connection handle
    def user_con(self, conn_sock):
        print("New connection!")
        csock, addr = conn_sock.accept()
        csock.send(("ACK").encode('UTF-8'))
        print("Send ACK")
        self.rqueue.append(csock)        # client socket
        user = User(usock=csock, uIP=addr)           
        self.user_list.append(user)      # user
        if user.usock == csock:
            print("Success")

    # Find who send the message
    def user_msg(self, s):
        
        print("User message")
        uflag = 0;
        
        for user in self.user_list:
            if uflag == 1:
                break
            if s == user.usock: # user send message
                uflag = 1;
                print("Matched: " + str(user.uname))
                data = s.recv(4096)
                if not data: # user leave
                    rid = user.roomID
                    print(user.uname + " leaves at room " + str(rid))
                    room = self.room_list[rid]
                    room.user_list.remove(user)
                    self.user_list.remove(user)
                    self.rqueue.remove(user.usock)
                msg = data.decode('UTF-8')
                self.user_msg_handle(s, user, msg)
        
        if uflag == 0:
            print("Non matched")
            data = s.recv(4096)
            print(data)
      
    # user message handle
    def user_msg_handle(self, s, user, msg):
        msg_list = msg.split(' ')
        
        # select service
        if msg_list[0] == "login":
            user.uname = msg_list[1]
            user.ustatus = "IDLE"
            s.send(("login ACK").encode('UTF-8'))
            print("New user: " + msg_list[1])
        
        # client asks for the informations: player list, room list
        elif msg_list[0] == "update":
            info = make_lobby_info(self.user_list, self.room_list)
            info = "update " + info
            s.send(info.encode('UTF-8'))
            print("Send: " + info)

        # client quits the game
        elif msg_list[0] == "quit":
            self.rqueue.remove(user.usock)
            self.user_list.remove(user)
            s.send("quit ACK".encode('UTF-8'))
            print("user quit")

        # client creates room
        elif msg_list[0] == "croom": # croom [room number] [room number]
            if len(msg_list) != 3 or int(msg_list[2]) < 4 or int(msg_list[2]) > 6:
                s.send(("croom DENY").encode('UTF-8'))
                print("Create room deny: wrong parameter")
            else:
                rid     = int(msg_list[1])
                max_num = int(msg_list[2])
                print("rid: " + str(rid) + " max_num: " + str(max_num))
                if rid < 0 or rid >= Server.ROOM_NUM or self.room_list[rid].rstatus != "EMPTY":
                    s.send(("croom DENY").encode('UTF-8'))
                    print("Create room deny: wrong room number")
                else:
                    user.ustatus        = "ROOM"
                    user.roomID         = rid
                    room = self.room_list[rid]
                    room.rstatus        = "WAIT"
                    room_user_list      = []
                    room_user_status    = []
                    room_user_list.append(user)
                    room.user_sock.append(s)
                    room_user_status.append("UNREADY")
                    room.user_list      = room_user_list
                    room.user_status    = room_user_status
                    room.max_unum       = max_num
                    room.status         = "WAIT"
                    s.send(("croom ACK").encode('UTF-8'))
                    print("Create room")
        
        # client goes to room
        elif msg_list[0] == "groom": # groom [room num]
            rid = int(msg_list[1])
            if rid < 0 or rid >= Server.ROOM_NUM:
                s.send(("groom DENY".encode('UTF-8')))
                print("Go to room deny")
            else:
                room = self.room_list[rid]
                if len(room.user_list) < room.max_unum:
                    user.ustatus = "ROOM"
                    user.roomID = rid
                    room.user_list.append(user)
                    room.user_sock.append(s)
                    room.user_status.append("UNREADY")
                    print("Go to room: " + str(rid))
                    s.send("groom ACK".encode('UTF-8'))
                else:
                    s.send(("groom DENY".encode('UTF-8')))
                    print("Go to room deny: room full")

        # client leaves the room
        elif msg_list[0] == "leave":
            rid = int(msg_list[1])
            if rid < 0 or rid >= Server.ROOM_NUM:
                s.send(("leave DENY".encode('UTF-8')))
                print("Leave room deny")
            else:
                room = self.room_list[rid]
                uindex = -1
                for i in range(len(room.user_list)):
                    if user.uIP == room.user_list[i].uIP:
                        uindex = i
                        break
                if uindex != -1: # find the client
                    del room.user_status[uindex]
                    del room.user_list[uindex]
                    user.ustatus = "IDLE"
                    s.send("leave ACK".encode('UTF-8'))
                    print("Leave ACK")
                else: # the client is not in this room
                    s.send(("leave DENY".encode('UTF-8')))
                    print("Leave room deny: client not in room")


        # client sets ready in the room
        elif msg_list[0] == "ready" or msg_list[0] == "unready":
            rid = int(msg_list[1])
            if rid < 0 or rid >= Server.ROOM_NUM:
                if msg_list[0] == "ready":
                    s.send("ready DENY".encode('UTF-8'))
                    print("ready error: wrong room id")
                else:
                    s.send("unready DENY".encode('UTF-8'))
                    print("unready error: wrong room id")
            
            else:
                rflag = -1
                for i in range(len(self.room_list[rid].user_list)):
                    if self.room_list[rid].user_list[i].usock == s:
                        rflag = i
                        break
                if rflag == -1:
                    if msg_list[0] == "ready":
                        s.send("ready DENY".encode('UTF-8'))
                        print("ready error: not in room")
                    else:
                        s.send("unready DENY".encode('UTF-8'))
                        print("unready error: not in room")
                else:
                    if msg_list[0] == "ready":
                        self.room_list[rid].user_status[rflag] = "READY"
                        s.send("ready ACK".encode('UTF-8'))
                        print(user.uname + " ready!")
                    else:
                        self.room_list[rid].user_status[rflag] = "UNREADY"
                        s.send("unready ACK".encode('UTF-8'))
                        print(user.uname + " unready!")
                    
                    # update every player
                    msg = self.make_room_update(rid)
                    for cs in self.room_list[rid].user_sock:
                        cs.send(msg.encode('UTF-8'))
                        ack_msg = cs.recv(4096)

        # client clicks start in the room
        elif msg_list[0] == "start":
            rid = int(msg_list[1])
            print(str(user.uname) + " clicks start! Room owner: " + str(self.room_list[rid].user_list[0].uname))
            if user.usock == self.room_list[rid].user_list[0].usock:
                print(str(user.uname) + " is the room owmer!")
                rflag = 1
                for i in range(len(self.room_list[rid].user_list)):
                    if self.room_list[rid].user_status[i] != "READY":
                        rflag = 0
                        print(str(self.room_list[rid].user_list[i].uname) + "'s status: " + self.room_list[rid].user_list[i].ustatus)
                        break

                if len(self.room_list[rid].user_list) != 0 and rflag == 1:
                    s.send("start ACK".encode('UTF-8'))
                    print("Start permitted")

                    # update status of user and room
                    for ustatus in self.room_list[rid].user_status:
                        ustatus = "GAME"
                    for u in self.room_list[rid].user_list:
                        u.ustatus = "GAME"
                    self.room_list[rid].rstatus = "GAME"    

                    # start judge
                    pipein, pipeout = os.pipe()
                    jport = rid + self.port_num + 10
                    pid = os.fork()

                    if pid == 0:
                        os.write(pipeout, "This message is from pipe".encode('UTF-8'))
                        judge_IP_list = []
                        for u in self.room_list[rid].user_list:
                            judge_IP_list.append(u.uIP)
                        judge = Judge(jID=len(self.judge_list), port=jport, room_in_charge=rid, IP_list=judge_IP_list)
                        judge.run()
                    
                    print("Fork judge")
                    time.sleep(1)
                    line = os.read(pipein, 32)
                    print(line.decode('UTF-8'))
                    for u in self.room_list[rid].user_list:
                        msg = "startgame " + str(jport)
                        u.usock.send(msg.encode('UTF-8'))

                    return
            
            s.send("start DENY".encode('UTF-8'))
            print("Start denied")

    # command msg
    def command(self):
        
        data = input()
        msg_list = data.split(" ")

        if msg_list[0] == "roomlist":
            self.show_roomlist()
            
        elif msg_list[0] == "userlist":
            self.show_userlist()

    # show room list
    def show_roomlist(self):
        for r in self.room_list:
            r.show_room()

    def show_userlist(self):
        for u in self.user_list:
            u.show_user()

    def make_room_update(self, rid):
        msg = "update " + str(len(self.room_list[rid].user_list))
        for i in range(len(self.room_list[rid].user_list)):
            msg += " " + self.room_list[rid].user_list[i].uname + " " + self.room_list[rid].user_status[i]
        return msg


def make_lobby_info(user_list, room_list):
    
    info = ""

    for user in user_list:
        info += str(user.uname) + ":" + str(user.ustatus) + "#"
    info += "%"
    
    for room in room_list:
        info += str(room.rID) + ":" + str(room.max_unum) + ":" + str(len(room.user_list)) + "#"
    
    return info

