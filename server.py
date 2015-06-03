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


# connection socket
conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn_sock.bind((socket.gethostname(), port_num))
conn_sock.listen(Server.MAX_PLAYER)

# reading queue
rqueue      = [conn_sock]

# server objct
server  = Server(rqueue)

# select timeout
timeout     = 1


while 1:
    
    rlist, wlist, elist = select.select(server.rqueue,[], [], timeout)

    for s in rlist:
        if s == conn_sock: # new connection
            print("New connection!")
            csock, addr = conn_sock.accept()
            csock.send(("ACK").encode('UTF-8'))
            print("Send ACK")
            server.rqueue.append(csock)        # client socket
            user = User(usock=csock)           
            server.user_list.append(user)      # user
            if user.usock == csock:
                print("Success")

        else:
            print("User")
            uflag = 0;
            for user in server.user_list:
                if uflag == 1:
                    break
                if s == user.usock: # user send message
                    # server.user_msg(s, user)
                    uflag = 1;
                    print("Matched")
                    data = s.recv(4096)
                    if not data: # user leave
                        print(user.uname + " leaves")
                        server.user_list.remove(user)
                        server.rqueue.remove(user.usock)
                    msg = data.decode('UTF-8')
                    msg_list = msg.split(' ')
                    
                    # select service
                    if msg_list[0] == "login":
                        user.uname = msg_list[1]
                        s.send(("login ACK").encode('UTF-8'))
                        print("New user: " + msg_list[1])
                    
                    elif msg_list[0] == "update":
                        info = make_lobby_info(server.user_list, server.room_list)
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
                            print("rid: " + str(rid) + " max_num: " + str(max_num))
                            if rid < 0 or rid >= Server.ROOM_NUM or server.room_list[rid].rstatus != "EMPTY":
                                s.send(("croom DENY").encode('UTF-8'))
                                print("Create room deny: wrong room number")
                            else:
                                room = server.room_list[rid]
                                room_user_list           = []
                                room_user_status         = []
                                room_user_list.append(user)
                                room_user_status.append("WAIT")
                                room.user_list      = room_user_list
                                room.user_status    = room_user_status
                                room.max_unum       = max_num
                                room.status         = "WAIT"
                                s.send(("croom ACK").encode('UTF-8'))
                                print("Create room")
                    
                    elif msg_list[0] == "groom": # groom [room num]
                        rid = int(msg_list[1])
                        if rid < 0 or rid >= Server.ROOM_NUM:
                            s.send(("groom DENY".encode('UTF-8')))
                            print("Go to room deny")
                        else:
                            room = server.romm_list[rid]
                            if len(room.user_list) < room.max_unum:
                                room.user_list.append(user)
                                room.user_status("WAIT")
                                print("Go to room: ")
                            else:
                                s.send(("groom DENY".encode('UTF-8')))
                                print("Go to room deny: room full")

                    elif msg_list[0] == "ready":
                        rid = int(msg_list)
                        if rid < 0 or rid >= Server.ROOM_NUM:
                            s.send("ready DENY".encode('UTF-8'))
                            print("ready error: wrong room id")
                        else:
                            s.send("ready ACK".encode('UTF-8'))
                            rflag = -1
                            for i in xrange(len(server.room_list[rid].user_list)):
                                if server.room_list[rid].user_list[i].usock == s:
                                    rflag = i
                                    break
                            if rflag == -1:
                                s.send("ready DENY".encode('UTF-8'))
                                print("ready error: not in room")
                            else:
                                server.room_list[rid].user_status[rflag] = "READY"
                                s.send("ready ACK".encode('UTF-8'))
                                print(user.uname + " ready!")

                if uflag == 0:
                    print("Non matched")
                    data = s.recv(4096)
                    print(data)



