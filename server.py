import sys
import select

from game_control import *
from server_kernel import *

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


# fake rooms
room = Room(roomID=123)
room_list.append(room)
room = Room(roomID=456)
room_list.append(room)
room = Room(roomID=789)
room_list.append(room)


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
                    msg = data.decode('UTF-8')
                    msg_list = msg.split(' ')
                    if msg_list[0] == "login":
                        user.uname = msg_list[1]
                        s.send(("ACK").encode('UTF-8'))
                        print("New user: " + msg_list[1])
                    elif msg_list[0] == "update":
                        info = make_lobby_info(user_list, room_list)
                        s.send(info.encode('UTF-8'))
                else:
                    print("Nonmatched")



