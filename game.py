import random


class Game:

    def __init__(self, player_num=0, hint=None, fail=None, num_card_left=0, players=[], garbage=[], hint_list=[], hanabi=[]):
        self.player_num = player_num
        self.hint = hint
        self.fail = fail
        #self.players = players
        self.players = [0 for x in range(self.player_num)]
        self.hint_list = []
        self.garbage = garbage
        self.hanabi=[0, 0, 0, 0, 0]
    
    def hit(self, player, cardidx, card_old, card_new):  # two cards are old and new respectively
        if (self.hanabi[card_old[0]] == card_old[1] - 1):
            self.hanabi[card_old[0]] = card_old[[1]
        else:
            self.garbage.append(card_old)
            self.fail -= 1
            if (self.fail == 0):
                #TODO
                print ('TODO...')
        self.players.update_card(cardidx, card_new)

    def throw(self, player, cardidx, card_old, card_new):
           self.garbage.append(card_old) 
        self.hint += 1
        self.players.update_card(cardidx, card_new)

    def hint(self, sender, recver, hinttype, number, card_idx):
        res = Hint(sender, recver, hinttype, number, card_idx)
        self.hint_list.append(res)
		self.hint -= 1

    def show_garbage(self):
        print ('Garbage ', end='')
        for i in range(len(self.garbage)):
            print (garbage[i], end='')
        print ('')

    def show_hanabi(self):
        print ('Hanabi ' + str(hanabi))
    
    def show_hint_list(self):
        print ('Hint_list ', end='')
        for i in range(len(self.hint_list)):
            print (str(hint_list), end='')
        print ('')

    def show_status(self):
        print ('Hint %d Fail %d' % (self.hint, self.fail))
        self.show_garbage()
        self.show_hanabi()
    
    def show_debug(self):
        for i in range(4):
            print ('>>> player %d ' % i, end='')
            self.players[i].debug()


class Game_player:

    def __init__(self, cards=[]):  # cards is a list of tuple(color_idx, number)
        self.cards = cards
    
    def update_card(self, cardidx, card):
        self.cards[cardidx] = card
    
    def debug(self):
        print (str(self.cards))


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
        else
            mtype = 'number'
        print ('[history] \'' + str(self.sender) + '\' hints \'' + str(self.recver) + \
               '\' type \'' + mtype + ' ' + str(self.number) + '\' card ' + str(self.card_idx))
