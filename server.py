import sys
import select

from game_control import *
from server_kernel import *

"""
Execution:
    python server.py [port number]
"""

# port number
port_num = int(sys.argv[1])

# maximum number of clients
MAX_PLAYER  = 20
ROOM_NUM    = 20

# connection socket
conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn_sock.bind((socket.gethostname(), port_num))
conn_sock.listen(MAX_PLAYER)

# user list
user_list   = []
room_list   = []
judge_list  = []

# reading queue
rqueue      = [conn_sock]
# select timeou
timeout     = 1

# rooms init
for i in xrange(ROOM_NUM):
    room = Room(rID=i)

while 1:
    
    rlist, wlist, elist = select.select(rqueue,[], [], timeout)

    for s in rlist:
        if s == conn_sock: # new connection
            print("New connection!")
            csock, addr = conn_sock.accept()
            csock.send(("ACK").encode('UTF-8'))
            print("Send ACK")
            rqueue.append(csock)        # client socket
            user = User(usock=csock)           
            user_list.append(user)      # user
            if user.usock == csock:
                print("Success")

        else:
            print("User")
            for user in user_list:
                if s == user.usock: # user send message
                    print("Matched")
                    data = s.recv(4096)
                    if not data: # user leave
                        print(user.uname + " leaves")
                        user_list.remove(user)
                        rqueue.remove(user.usock)
                    msg = data.decode('UTF-8')
                    msg_list = msg.split(' ')
                    if msg_list[0] == "login":
                        user.uname = msg_list[1]
                        s.send(("login ACK").encode('UTF-8'))
                        print("New user: " + msg_list[1])
                    elif msg_list[0] == "update":
                        info = make_lobby_info(user_list, room_list)
                        info = "update " + info
                        s.send(info.encode('UTF-8'))
                        print("Send: " + info)

                    elif msg_list[0] == "croom": # croom [room number] [room number]
                        if len(msg_list) != 3 or int(msg_list[2]) < 4 or int(msg_list[2]) > 6:
                            s.send(("croom DENY").encode('UTF-8'))
                            print("Create room deny: wrong parameter")
                        else:
                            rid     = int(msg_list[1])
                            max_num = int(msg_list[2])
                            if rid < 0 or rid >= ROOM_NUM or \
                                    room_list[rid].status != "EMPTY":
                                s.send(("croom DENY").encode('UTF-8'))
                                print("Create room deny: wrong room number")
                            else:
                                room = room_list[rid]
                                user_list           = []
                                user_status         = []
                                user_list.append(user)
                                user_status.append("WAIT")
                                room.user_list      = user_list
                                room.user_status    = user_status
                                room.max_unum       = max_num
                                room.status         = "WAIT"
                                s.send(("croom ACK").encode('UTF-8'))
                                print("Create room")
                    elif msg_list[0] == "groom": # groom [room num]
                        rid = int(msg_list[1])
                        if rid < 0 or rid >= ROOM_NUM:
                            s.send(("groom DENY".encode('UTF-8')))
                            print("Go to room deny")
                        else:
                            room = romm_list[rid]
                            if len(room.user_list) < room.max_unum:
                                room.user_list.append(user)
                                room.user_status("WAIT")
                                print("Go to room: ")
                            else:
                                s.send(("groom DENY".encode('UTF-8')))
                                print("Go to room deny: room full")

                else:
                    print("Non matched")
                    data = user.recv(4096)
                    print(data)



