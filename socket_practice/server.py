import sys
import os
import time
import socket

from judge import judge


def main():
    server_port = int(sys.argv[1])
    judge_port = int(sys.argv[2])
    player_num = int(sys.argv[3])

    ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssock.bind((socket.gethostname(), server_port))
    ssock.listen(10)
    csocklist = []
    caddrlist = []

    while 1:
        (csock, address) = ssock.accept()
        csocklist.append(csock)
        caddrlist.append(address)
        if(len(csocklist) == player_num):
            pid = os.fork()
            if pid == 0:
                # child
                myjudge = judge(judge_port, player_num)
                myjudge.run()
            # send judge info to clients
            time.sleep(1)
            for i in xrange(player_num):
                csocklist[i].send(str(judge_port))


if __name__ == '__main__':
    main()
