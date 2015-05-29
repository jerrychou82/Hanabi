import socket
import sys


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.connect(("linux6.csie.ntu.edu.tw", int(sys.argv[1])))
    sock.connect((sys.argv[1], int(sys.argv[2])))

    msg = sock.recv(1024)
    #judge_port = int(msg)
    msg = msg.decode('UTF-8')
    print ('rev msg ' + msg)

    #print "judge port " + str(judge_port)
    #jsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #jsock.connect(("linux6.csie.ntu.edu.tw", judge_port))
    #msg = jsock.recv(1024)
    #print msg
