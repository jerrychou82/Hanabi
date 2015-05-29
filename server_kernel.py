from game_control import *

def make_lobby_info(user_list, room_list):
    
    info = "user#"

    for user in user_list:
        info += user.uname + ":" + user.status + "#"
    info += "%"
    
    for room in room_list:
        info += str(room.roomID) + ":" + str(room.max_unum) + ":" + str(len(room.user_list)) + "#"
    
    return info

