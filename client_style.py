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
        print("|                     |                    |")
        print("+------------------------------------------+")
        print()


class Room_Style:
    
    @staticmethod
    def print_room(rid, uID, room_list):
        os.system('clear')
        num_player = len(room_list)
        
        # os.system('clear')
        print("+------------------------------------------+")
        print("| \x1b[1,35mPlayer%d" % uID + "\x1b[0m          Room%d" % rid  + "                   |")
        print("+------------------------------------------+")
        print("| \x1b[1;34mHost\x1b[0m        |              |             |")
        print("|             |              |             |")
        print("|    "\
                + ("\x1b[1;31m" if room_list[0][1] == "READY" else "\x1b[1;30m") + "Ready" + "\x1b[0m" + "    |     " \
                + ("\x1b[1;31m" if room_list[1][1] == "READY" else "\x1b[1;30m") + "Ready" + "\x1b[0m" + "    |    " \
                + ("\x1b[1;31m" if room_list[2][1] == "READY" else "\x1b[1;30m") + "Ready" + "\x1b[0m" + "    |")
        print("|             |              |             |")
        print("|  %8s" % room_list[0][0]  + "   |   %8s" % room_list[1][0] + "   |  %8s" % room_list[2][0] + "   |")
        print("+-------------+--------------+-------------+")
        print("|             |              |             |")
        print("|             |              |             |")
        print("|    "\
                + ("\x1b[1;31m" if room_list[3][1] == "READY" else "\x1b[1;30m") + "Ready" + "\x1b[0m" + "    |     " \
                + ("\x1b[1;31m" if room_list[4][1] == "READY" else "\x1b[1;30m") + "Ready" + "\x1b[0m" + "    |    " \
                + ("\x1b[1;31m" if room_list[5][1] == "READY" else "\x1b[1;30m") + "Ready" + "\x1b[0m" + "    |")
        print("|             |              |             |")
        print("|  %8s" % room_list[3][0]  + "   |   %8s" % room_list[4][0] + "   |  %8s" % room_list[5][0] + "   |")
        print("+------------------------------------------+")
        
        # for user in room_list:
            # print(user[0] + " " + user[1])


