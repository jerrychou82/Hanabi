import random
import os

class Game:

    @staticmethod
    def print_cards(cards):
        print()
        if len(cards) == 0:
            return
        print_msg = [""] * 3
        for card in cards:
            msg = Game.print_card(card)
            for i in range(3):
                print_msg[i] += msg[i]
        for i in range(3):
            print(print_msg[i])
        
    @staticmethod
    def print_card(card):
        msg = []
        msg.append(" +---+ ")
        msg.append(" | \x1b[1;%dm" % (30 + card[0])  + (str(card[1]) if card[1] != -1 else "?") \
                    + "\x1b[0m | ")
        msg.append(" +---+ ")
        return msg


    def __init__(self, player_num=0, hint=8, fail=0, num_card_left=0, garbage=[], hint_list=[], hanabi=[], buf=""):
        self.player_num     = player_num
        self.hint_num       = hint
        self.fail_num       = fail
        self.num_card_left  = 50 - player_num * 4
        self.hint_list      = []
        self.garbage        = []
        self.hanabi         = [0, 0, 0, 0, 0]
        self.buf            = buf
        self.players_init(buf)
    
    def hit(self, player, cardidx, card_old, card_new):  # two cards are old and new respectively
        print ('card_old ' + str(card_old))
        print ('card_new ' + str(card_new))
        if (self.hanabi[card_old[0] - 1] == card_old[1] - 1):
            self.hanabi[card_old[0] - 1] = card_old[1]
        else:
            self.garbage.append(card_old)
            self.fail_num += 1
            if (self.fail_num == 3):
                #TODO
                print ('fail == 0...QQ')
                print ('TODO...')
        self.players[player].update_card(cardidx, card_new)
        self.num_card_left -= 1

    def throw(self, player, cardidx, card_old, card_new):
        self.garbage.append(card_old) 
        if (self.hint_num < 8):
            self.hint_num += 1
        self.players[player].update_card(cardidx, card_new)
        self.num_card_left -= 1

    def hint(self, sender, recver, hinttype, number, card_idx):
        res = Hint(sender, recver, hinttype, number, card_idx)
        self.hint_list.append(res)
        self.hint_num -= 1

    def show_garbage(self):
        print ('Garbage ', end='')
        # for i in range(len(self.garbage)):
            # print (self.garbage[i], end='')
        Game.print_cards(self.garbage)
        print ()

    def show_hanabi(self):
        # print ('Hanabi ' + str(self.hanabi))
        cards = []
        for i in range(5):
            cards.append((i+1,self.hanabi[i]))
        Game.print_cards(cards)

    def show_hint_list(self):
        print ('Hint_list:')
        for i in range(len(self.hint_list)):
            self.hint_list[i].show_hint()

    def show_status(self):
        os.system('clear')
        print ('player_num %d Hint %d Fail %d' % (self.player_num, self.hint_num, self.fail_num))
        self.show_garbage()
        self.show_hanabi()
        self.show_hint_list()
        for i in range(self.player_num):
            print ('>>> player %d ' % i, end='')
            self.players[i].debug()

    def players_init(self, buff):
        print ('buf ->>>>>>> %s.' % buff)
        self.players = ['None'] * self.player_num
        buf = buff.split(' ')
        # handle serve result
        for i in range(self.player_num):
            print("player" + str(i) + ": ")
            card_list = []
            for j in range(4):
                card = (int(buf[2+8*i+2*j+1]), int(buf[2+8*i+2*j+2]))
                card_list.append(card)
                print("  (" + str(buf[2+8*i+2*j+1]) + ", " + str(buf[2+8*i+2*j+2]) + ")")
            self.players[i] = Game_player(cards=card_list)
    
    def get_score(self):
        return sum(self.hanabi)


class Game_player:

    def __init__(self, cards=[]):  # cards is a list of tuple(color_idx, number)
        print(cards)
        self.cards = cards
    
    def update_card(self, cardidx, card):
        self.cards[cardidx] = card
    
    def debug(self):
        # print (str(self.cards))
        Game.print_cards(self.cards)


class Hint:

    def __init__(self, sender=None, recver=None, hinttype=None, number=None, card_idx=[]):
        self.sender = sender
        self.recver = recver
        self.hinttype = hinttype
        self.number = number
        self.card_idx = card_idx

    def show_hint(self):
        mtype = 'undefined'
        if (self.hinttype == 0):
            mtype = 'color'
        else:
            mtype = 'number'
        print ('[history] \'' + str(self.sender) + '\' hints \'' + str(self.recver) + \
               '\' type \'' + mtype + ' ' + str(self.number) + '\' card ' + str(self.card_idx))
