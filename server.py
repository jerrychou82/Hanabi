import socket
import sys
import select

from game_control import *

# port number
port_num = int(sys.argv[1])

# maximum number of clients
MAX_PLAYER = 20

# connection socket
conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn_sock.bind((socket.gethostname(), port_num))
conn_sock.listen(MAX_PLAYER)

# user list
user_list = []
room_list = []
judge_list = []

# reading queue
rqueue = [conn_sock]
# select timeou
timeout = 1

while 1:
    
    rlist, wlist, elist = select.select(rqueue,[], [], timeout)

    for s in rlist:
        if s == conn_sock: # new connection
            csock, addr = conn_sock.accept()
            csock.send("ACK")
            rqueue.append(csock)        # client socket
            user = User(csock)           
            user_list.append(user)      # user

        else:
            for user in user_list:
                if s == user.sock:
                    msg = s.recv(4096)
                    msg_list = msg.split(' ')
                    if msg_list[0] == "login":
                        user.uname = msg_list[1]
                        print("New user: " + msg_list[1])




