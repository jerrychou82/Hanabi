import socket
import select
import sys

from game_control import *

'''
usage: python3 client.py [host] [port]
'''

user_list = []
room_list = []
ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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


def dump_roomlist(u_list):
    print ('dumping room list...')
    for r in r_list:
        print ('\trID ' + r.rID + ' max_unum ' + r.max_unum + ' cur_unum ' + r.cur_unum)


def main():
    if (len(sys.argv) != 3):
        print ('usage: python3 client.py [server addr] [port]')
        return

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
        if (msg == 'login ACK'):
            break
    

    while (True):
        print ('Now in lobby!')
        print ('before select')
        (inputready, outputready, exceptrdy) = select.select([0, ssock], [], [])

        for i in inputready:
            if (i == 0):
                #TODO
                buff = input()
                buf = buff.split(' ')
                msg = buf[0]
                if (msg == 'update'):
                    print ('Now update...')
                    update = 'update'
                    ssock.send(update.encode('UTF-8'))
                    data = ssock.recv(4096)
                    print (data.decode('UTF-8'))
                    data2 = data.decode('UTF-8')  #will receive 'update #fro11o:CONN#...#%#123:4:0#...#'
                    data3 = data2.split(' ')  #erase update

                    user_list[:] = []
                    room_list[:] = []
                    res = data3[1].split('%')
                    print (res)
                    user = res[0].split('#')
                    room = res[1].split('#')
                    print (user)
                    print (room)
                    for u in user:
                        if (u == ''):
                            continue
                        ui = u.split(':')    
                        uu = Unode(uname=ui[0], ustatus=ui[1])
                        user_list.append(uu)
                    dump_userlist(user_list)
                    for r in room:
                        if (r == ''):
                            continue
                        ri = r.split(':')
                        rr = Rnode(rID=ri[0], max_unum=ri[1], cur_unum=r[2])
                    dump_roomlist(room_list)

                        

                elif (msg == 'croom'):
                    print ('Now croom...')
                    if (len(buf) != 3 or is_number(buf[2]) == False):
                        print ('wrong usage! croom [room_name] [max_number]')
                        continue

                    ssock.send(buf.encode('UTF-8'))  #TODO if this message lose
                    data = ssock.recv(4096)
                    #TODO fork to room process?
                    while (True):
                        print ('what i recv is ' + data.decode('UTF-8'))
                        if (data.decode('UTF-8') == 'croom ACK'):
                            print ('croom success')

                elif (msg == 'groom'):
                    print ('Now groom...')
                    #TODO need to do thing here or in room process? need discussing...
                else:
                    print ('nani?')
            else:
                print ('recv from server automatically ^.<')
                buff = ssock.recv(4096)
                buf = (buff.decode('UTF-8')).split(' ')
                if (buf[0] == 'update'):
                    user_list[:] = []
                    room_list[:] = []
                    res = buf[1].split('%')
                    print (res)
                    user = res[0].split('#')
                    room = res[1].split('#')
                    print (user)
                    print (room)
                    user_list[:] = []
                    room_list[:] = []
                    for u in user:
                        if (u == ''):
                            continue
                        ui = u.split(':')    
                        uu = Unode(uname=ui[0], ustatus=ui[1])
                        user_list.append(uu)
                    dump_userlist(user_list)
                    for r in room:
                        if (r == ''):
                            continue
                        ri = r.split(':')
                        rr = Rnode(rID=ri[0], max_unum=ri[1], cur_unum=r[2])
                    dump_roomlist(room_list)
                else:
                    print ('nani?')
    


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
