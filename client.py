import socket
import select
import sys

from game_control import *


user_list = []

def main():
    if (len(sys.argv) != 3):
        print ('usage: python3 client.py [server addr] [port]')
        return
        


    ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssock.connect((sys.argv[1], int(sys.argv[2])))

    while (True):
        data = ssock.recv(4096)
        msg = data.decode('UTF-8')
        if (msg == 'ACK'):
            break

    nickname = input('Please enter nickname: ')
    print ('sending nickname to server...')
    msg = 'login ' + nickname
    ssock.send(msg.encode('UTF-8'))
    print ('after send')

    while (True):
        data = ssock.recv(4096)
        print ('recv ' + data.decode('UTF-8'))
        msg = data.decode('UTF-8')
        if (msg == 'ACK'):
            break
    
    print ('Now in lobby!')

    while (True):
        print ('before select')
        (inputready, outputready, exceptrdy) = select.select([0, ssock], [], [])

        for i in inputready:
            if (i == 0):
                #TODO
                msg = input()
                update = 'update'
                ssock.send(update.encode('UTF-8'))
                data = ssock.recv(4096)
                print (data.decode('UTF-8'))
                data2 = data.decode('UTF-8')
                res = data2.split('%')


            else:
                update = 'update'
                #TODO
                ssock.recv(4096)
    
def dump_userlist():
    print ('dumping user list...')
    for u in user_list:
        print ('\tuser ' + u.uname + ' status ' + u.status)


if __name__ == '__main__':
    user_list[:] = []
    s = '#fro11o:CONN#%123:4:0#456:4:0#789:4:0#'
    res = s.split('%')
    print (res)
    user = res[0].split('#')
    print (user)
    for u in user:
        if (u == ''):
            continue
        ui = u.split(':')    
        uu = User(username=ui[0], status=ui[1])
        user_list.append(uu)
    dump_userlist()
    #room = res[1].split('#')
    #main()
