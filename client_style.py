import os

class Login:
    
    @staticmethod
    def print_login():
        os.system('clear')
        print("+------------------------------------------+")
        print("|                                          |")
        print("|               Welcome to                 |")
        print("|                                          |")
        print("| *   *    *    *    *    *    ****   ***  |")
        print("| *   *   * *   **   *   * *   *   *   *   |")
        print("| *   *   * *   * *  *   * *   *   *   *   |")
        print("| *****   ***   *  * *   ***   ****    *   |")
        print("| *   *  *   *  *  * *  *   *  *   *   *   |")
        print("| *   *  *   *  *   **  *   *  *   *   *   |")
        print("| *   * *     * *    * *     * ****   ***  |")
        print("|                                          |")
        print("|              2015 NTU CSIE               |")
        print("|                                          |")
        print("|    Andy fro11o Jerry mid Fukao ChiDo     |")
        print("|                                          |")
        print("+------------------------------------------+")
        print()
        nickname = input("Please enter your name: ")
        return nickname


class Lobby:
    
    @staticmethod
    def print_lobby(user_list, room_list):
        os.system('clear')
        print("+------------------------------------------+")
        print("|                  Lobby                   |")
        print("+------------------------------------------+")
        print("|        Room         |        User        |")
        print("+---------------------+--------------------+")
        print("|  ID    Num    Max   |  Name     Status   |")
        print("|                     |                    |")

        N = max(len(user_list), len(room_list))
        for i in range(N):
            if i < len(room_list):
                msg = "|  %2d" % room_list[i].rID + "     " + str(room_list[i].cur_unum) + "      " + str(room_list[i].max_unum) + "    |"
            else:
                msg = "                     |"
            if i < len(user_list):
                msg += "  %8s" % user_list[i].uname + " %6s" % user_list[i].ustatus + "   |"
            else:
                msg += "                    |"
            print(msg)
        '''
        for u in user_list:
            print ('\tuser ' + u.uname + ' status ' + u.ustatus)
        for r in room_list:
            print ('\trID ' + str(r.rID) + ' max_unum ' + str(r.max_unum) + ' cur_unum ' + str(r.cur_unum))
        '''
        print("|                     |                    |")
        print("+------------------------------------------+")
        print()


class Room_Style:
    
    @staticmethod
    def print_room(rid, room_list):
        print(room_list)
        num_player = len(room_list)
        print(num_player)
        for i in range(6 - num_player):
            room_list.append(("", ""))
        line = "|  %8s" % room_list[0][0]  + "   |   %8s" % room_list[1][0] + "   |  %8s" % room_list[2][0] + "   |"
        
        os.system('clear')
        print("+------------------------------------------+")
        print("|                  Room%d" % rid  + "                   |")
        print("+------------------------------------------+")
        print("| \x1b[1;34mHost\x1b[0m        |              |             |")
        print("|             |              |             |")
        print("|             |              |             |")
        print("|             |              |             |")
        print(line)
        print("|  %8s" % room_list[0][0]  + "   |   %8s" % room_list[1][0] + "   |  %8s" % room_list[2][0] + "   |")
        print("+-------------+--------------+-------------+")
        print("|             |              |             |")
        print("|             |              |             |")
        print("|             |              |             |")
        print("|             |              |             |")
        print("|             |              |             |")
        print("+------------------------------------------+")
        for user in room_list:
            print(user[0] + " " + user[1])


