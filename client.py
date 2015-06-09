import socket
import select
import sys
import time

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
        print ('\tuser ' + u.uname + ' status ' + u.ustatus)


def dump_roomlist(r_list):
    print ('dumping room list...')
    for r in r_list:
        print ('\trID ' + str(r.rID) + ' max_unum ' + str(r.max_unum) + ' cur_unum ' + str(r.cur_unum))


def sJudge(hanabi_addr, rID, jport):  #TODO maybe should have some arguments...?
    print ('[judge ' + str(rID) + '] inside judge XD')

    print ('Now connect to ' + str(hanabi_addr) + ':' + str(jport) + '...')
    jsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    jsock.connect((str(hanabi_addr), jport))

    gameID = -1
    game_player_num = -1

    while (True):  # game init
        print ('[judge ' + str(rID) + '] waiting for judge command...')
        (inputready, outputready, exceptrdy) = select.select([0, ssock, jsock], [], [])

        ok = False
        for i in inputready:
            if i == 0:
                data = input()
                print ('[judge ' + str(rID) + '] what you type is \'' + data + '\'')
                #TODO...
            elif i == ssock:
                data = ssock.recv(4096)  # take those msg, it must be 'startgame portID'
                print ('[judge ' + str(rID) + '] recv from ssock \'' + data.decode('UTF-8') + '\'')
                time.sleep(2)
                tmp = 'startgame ACK'
                ssock.send(tmp.encode('UTF-8'))
            elif i == jsock:
                data = jsock.recv(4096)
                print ('[judge ' + str(rID) + '] recv from jsock \'' + data.decode('UTF-8') + '\'')
                time.sleep(2)
                buff = data.decode('UTF-8')
                buf = buff.split(" ")
                if (buf[0] == 'startgame'): # stargame and serve result
                    ok = True
                    gameID = int(buf[1])
                    game_player_num = int(buf[2])
                    # handle serve result
                    for i in range(game_player_num):
                        print("player" + str(i) + ": ")
                        for j in range(4):
                            print("  (" + str(buf[2+8*i+2*j+1]) + ", " + str(buf[2+8*i+2*j+2]) + ")")

                    break
        if (ok == True):
            break

    while (True):  # game loop
        print ('[judge ' + str(rID) + '] inside game loop XD')
        (inputready, outputready, exceptrdy) = select.select([0, jsock], [], [])
        for i in inputready:
            if i == 0:
                print ('TODO...')
            elif i == jsock:
                data = jsock.recv(4096)
                msg = data.decode('UTF-8')
                msg_list = msg.split(' ')

                if msg_list[0] == "yourturn":
                    # jsock.send("hit 1".encode('UTF-8'))
                    jsock.send("hint 1 0 4".encode('UTF-8'))
                    # jsock.send("throw 2".encode('UTF-8'))


def sRoom(hanabi_addr, ssock, rID):  #TODO In fact this function will have a port input and create a new socket itself
    print ('[room ' + str(rID) + '] inside room XD')

    leave = False

    while (True):
        print ('[room ' + str(rID) + '] waiting for user command...')
        (inputready, outputready, exceptrdy) = select.select([0, ssock], [], [])
        for i in inputready:
            if i == 0:
                buff = input()
                buf = buff.split(' ')
                if (len(buf) == 2 and buf[0] == 'ready' and is_number(buf[1])):
                    tmp = 'ready ' + str(rID)
                    print ('[room ' + str(rID) + '] i will send \'' + tmp + '\'')
                    ssock.send(tmp.encode('UTF-8'))
                elif (len(buf) == 2 and buf[0] == 'unready' and is_number(buf[1])):
                    tmp = 'unready ' + str(rID)
                    print ('[room ' + str(rID) + '] i will send \'' + tmp + '\'')
                    ssock.send(tmp.encode('UTF-8'))
                elif (len(buf) == 2 and buf[0] == 'start' and is_number(buf[1])):
                    tmp = 'start ' + str(rID)
                    print ('[room ' + str(rID) + '] i will send \'' + tmp + '\'')
                    ssock.send(tmp.encode('UTF-8'))
                elif (len(buf) == 2 and buf[0] == 'leave' and is_number(buf[1])):
                    tmp = 'leave ' + str(rID)
                    print ('[room ' + str(rID) + '] i will send \'' + tmp + '\'')
                    time.sleep(2)
                    ssock.send(tmp.encode('UTF-8'))
                else:
                    print ('nothing happen')
            if i == ssock:
                data = ssock.recv(4096)
                print ('[room ' + str(rID) + '] recv from server \'' + data.decode('UTF-8') + '\'')
                buf = (data.decode('UTF-8')).split(" ")
                if (len(buf) == 2 and buf[0] == 'startgame' and is_number(buf[1])):
                    tmp = 'startgame ACK'
                    ssock.send(tmp.encode('UTF-8'))
                    sJudge(hanabi_addr, rID, int(buf[1]))
                elif (len(buf) == 2 and buf[0] == 'leave' and buf[1] == 'ACK'):
                    leave = True
                    break

        if (leave == True):
            break


def main():
    if (len(sys.argv) != 3):
        print ('usage: python3 client.py [server addr] [port]')
        return

    hanabi_addr = sys.argv[1]
    ssock.connect((hanabi_addr, int(sys.argv[2])))

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
        print ('wait for ACK from server')
        data = ssock.recv(4096)
        print ('recv ' + data.decode('UTF-8'))
        msg = data.decode('UTF-8')
        if (msg == 'login ACK'):
            break
    
    byebye = False

    while (True):
        print ('Now in lobby!')
        print ('before select')
        (inputready, outputready, exceptrdy) = select.select([0, ssock], [], [])

        for i in inputready:
            if (i == 0):  # select from stdin
                #TODO
                buff = input()
                buf = buff.split(' ')

                if (len(buf) < 1):
                    print ('error: does not get any msg')
                    continue

                msg = buf[0]
                if (msg == 'update'):
                    print ('Now update...')
                    update = 'update'
                    ssock.send(update.encode('UTF-8'))
                    data = ssock.recv(4096)
                    print ('recv \'' + data.decode('UTF-8') + '\' from server')
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

                        tmp = []
                        for tt in ri:
                            if (tt == ' '):
                                continue
                            tmp.append(int(tt))

                        rr = Rnode(rID=tmp[0], max_unum=tmp[1], cur_unum=tmp[2])
                        room_list.append(rr)
                    dump_roomlist(room_list)

                elif (msg == 'croom'):
                    print ('Now croom...')
                    if (len(buf) != 3 or is_number(buf[1]) == False or is_number(buf[2]) == False):
                        print ('wrong usage! croom [room_number] [max_number]')
                        continue

                    print ('i will send \'' + buff + '\'')
                    time.sleep(2)
                    ssock.send(buff.encode('UTF-8'))  #TODO if this message lose
                    #TODO fork to room process?
                    while (True):
                        data = ssock.recv(4096)
                        print ('what i recv is ' + data.decode('UTF-8'))
                        if (data.decode('UTF-8') == 'croom ACK'):  #it will have port number later...
                            print ('croom success')
                            sRoom(hanabi_addr, ssock, int(buf[1]))
                            break
                        else:
                            print ('croom fail')
                            break

                elif (msg == 'groom'):
                    print ('Now groom...')
                    #TODO need to do thing here or in room process? need discussing...
                    if (len(buf) != 2 or is_number(buf[1]) == False):
                        print ('wrong usage! groom [room_number]')
                        continue

                    print ('i will send \'' + buff + '\'')
                    time.sleep(2)
                    ssock.send(buff.encode('UTF-8'))

                    while (True):
                        data = ssock.recv(4096)
                        print ('what i recv is ' + data.decode('UTF-8'))
                        if (data.decode('UTF-8') == 'groom ACK'):
                            print ('groom success')
                            sRoom(hanabi_addr, ssock, int(buf[1]))
                            break
                        else:
                            print ('groom fail')
                            break
                
                elif (msg == 'quit'):
                    print ('Now quit...')
                    
                    ssock.send(msg.encode('UTF-8'))

                    while (True):
                        data = ssock.recv(4096)
                        print ('what i recv is ' + data.decode('UTF-8'))
                        if (data.decode('UTF-8') == 'quit ACK'):
                            print ('quit success')
                            byebye = True
                            break

                else:
                    print ('nani?')

            else:  # select from ssock
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
                    print ('Now dumping user_list')
                    dump_userlist(user_list)
                    for r in room:
                        if (r == ''):
                            continue
                        ri = r.split(':')
                        rr = Rnode(rID=ri[0], max_unum=ri[1], cur_unum=r[2])
                        item_list.append(rr)
                    print ('Now dumping item_list')
                    dump_roomlist(room_list)
                else:
                    print ('nani?')
    
        if (byebye == True):
            break

    ssock.close()


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
