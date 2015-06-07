import random


class Game:

    def __init__(self, player_num=0, desk=[], hint=None, fail=None, players=[], hint_list=[], garbage=[], hanabi=[]):
		self.player_num = player_num
        self.desk = desk
        self.hint = hint
        self.fail = fail
        #self.players = players
        self.players = [0 for x in range(self.player_num)]
        self.hint_list = []
        self.garbage = garbage
        self.hanabi=[0, 0, 0, 0, 0]
    
    def serve(self, player, cards):
        self.players[player] = Game_player(cards)

	def hit(self, player, cardidx, card):
		self.players[player].update_card(cardidx], card)

	def throw(self, player, cardidx, card):
		self.players[player].update_card(cardidx], card)

	def add_hint(self, sender, recver, hinttype, cards):
		res = Hint(sender, recver, hinttype, cards)
		self.hint_list.append(res)

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


class Game_player:

    def __init__(self, cards=[]):  # cards is a list of tuple(color_idx, number)
        self.cards = cards
    
    def update_card(cardidx, card):
        self.cards[cardidx] = card


class Hint:

    def __init__(self, sender=None, recver=None, hinttype=None, cards=[]):
		self.sender = sender
		self.recver = recver
		self.hinttype = hinttype
		self.cards = cards

    def show_hint(self):
        mtype = 'undefined'
        if (self.hinttype == 0):
            mtype = 'color'
        else
            mtype = number
        print ('[history] \'' + str(sender) + '\' hints \'' + str(recver) + \
               '\' type \'' + mtype + '\' card ' + str(self.cards))
