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
rqueue      = [0, conn_sock]

# server objct
server  = Server(rqueue)

# select timeout
timeout     = 1


while 1:
    
    rlist, wlist, elist = select.select(server.rqueue,[], [], timeout)

    for s in rlist:
        
        if s == 0:
            server.command()

        # new connection
        elif s == conn_sock:
            server.user_con(conn_sock)

        # message
        else:
            server.user_msg(s)

        
