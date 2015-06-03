from game_control import *

class Server:
        
    # maximum number of clients
    MAX_PLAYER  = 20
    ROOM_NUM    = 20

    def __init__(self, rqueue): 
    
        # list
        self.user_list  = []
        self.room_list  = []
        self.judge_list = []
        
        # rooms init
        for i in xrange(Server.ROOM_NUM):
            room = Room(rID=i)
            self.room_list.append(room)
        
        # reading queue
        self.rqueue          = rqueue

    def user_msg(self, s):
        


def make_lobby_info(user_list, room_list):
    
    info = ""

    for user in user_list:
        info += user.uname + ":" + user.ustatus + "#"
    info += "%"
    
    for room in room_list:
        info += str(room.rID) + ":" + str(room.max_unum) + ":" + str(len(room.user_list)) + "#"
    
    return info

