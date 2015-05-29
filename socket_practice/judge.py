import socket
import sys

class judge(object):

    def __init__(self, port, n_player):
        self.port = port
        self.n_player = n_player
    
    def run(self):
        
        jsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #jsock.bind((socket.gethostname(), self.port))
        jsock.bind(('', self.port))
        jsock.listen(self.n_player)
        csocklist = []
        caddrlist = []
        while (len(csocklist) < self.n_player):
            (csock, caddr) = jsock.accept()
            csocklist.append(csock)
            caddrlist.append(caddr)
            #assert (len(csocklist) == len(caddrlist))

        check = [False for x in range(4)]
		jsock.setblocking(0)
		while (True):
		    for i in range(4):
			    scosklist[i].send(bytes('Hello player_' + str(i) + '!', 'UTF-8'))
			


    	msg = sock.recv(1024)


if __name__ == '__main__':
	J = judge(65005, 4)
	J.run()
