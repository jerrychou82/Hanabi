import socket
import select
import sys

from game_control import *


user_list = []

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def dump_userlist(u_list):
    print ('dumping user list...')
    for u in u_list:
        print ('\tuser ' + u.uname + ' status ' + u.status)

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
    

    while (True):
        print ('Now in lobby!')
        print ('before select')
        (inputready, outputready, exceptrdy) = select.select([0, ssock], [], [])

        for i in inputready:
            if (i == 0):
                #TODO
                buf = input()
                msg = buf[0]
                if (msg == 'update'):
                    print ('Now update...')
                    ssock.send(update.encode('UTF-8'))
                    data = ssock.recv(4096)
                    print (data.decode('UTF-8'))
                    data2 = data.decode('UTF-8')

                    user_list[:] = []
                    res = data2.split('%')
                    print (res)
                    user = res[0].split('#')
                    print (user)
                    for u in user:
                        if (u == ''):
                            continue
                        ui = u.split(':')    
                        uu = User(username=ui[0], status=ui[1])
                        user_list.append(uu)
                    dump_userlist(user_list)
                elif (msg == 'croom'):
                    print ('Now croom...')
                    if (len(buf) != 3 or is_number(buf[2]) == False):
                        print ('wrong usage! croom [room_name] [max_number]')
                        continue

                    ssock.send(buf.encode('UTF-8'))  #TODO if this message lose
                    data = ssock.recv(4096)
                    #TODO fork to room process?

                elif (msg == 'groom'):
                    print ('Now groom...')
                    #TODO need to do thing here or in room process? need discussing...
                else:
                    print ('nani?')
            else:
                update = 'update'
                #TODO
                ssock.recv(4096)
    


if __name__ == '__main__':
    main()
    '''
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
    dump_userlist(user_list)
    '''
