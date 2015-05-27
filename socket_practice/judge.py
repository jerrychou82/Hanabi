import socket
import sys

class judge(object):

    def __init__(self, port, n_player):
        self.port = port
        self.n_player = n_player
    
    def run(self):
        
        jsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        jsock.bind((socket.gethostname(), self.port))
        jsock.listen(self.n_player)
        csocklist = []
        caddrlist = []
        while (len(csocklist) < self.n_player):
            (csock, caddr) = jsock.accept()
            csocklist.append(csock)
            caddrlist.append(caddr)
            #assert (len(csocklist) == len(caddrlist))
        csocklist[0].send('Hello 0!')
        csocklist[1].send('Hello 1!')

