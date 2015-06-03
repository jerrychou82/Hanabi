from game_control import *

def make_lobby_info(user_list, room_list):
    
    info = ""

    for user in user_list:
        info += user.uname + ":" + user.ustatus + "#"
    info += "%"
    
    for room in room_list:
        info += str(room.rID) + ":" + str(room.max_unum) + ":" + str(len(room.user_list)) + "#"
    
    return info

