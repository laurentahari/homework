import random
import unittest

# SI 206 Fall 2017
# Homework 3 - Code

##COMMENT YOUR CODE WITH:
# Section Day/Time: Thursday 6-7pm
# People you worked with:

######### DO NOT CHANGE PROVIDED CODE #########
### Below is the same cards.py code you saw in lecture.
### Scroll down for assignment instructions.
#########


##**##**##**##@##**##**##**## # DO NOT CHANGE OR DELETE THIS COMMENT LINE -- we use it for grading your file
###############################################

### Write unit tests below this line for the cards code above.
class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)


def play_war_game(testing=False):
	# Call this with testing = True and it won't print out all the game stuff -- makes it hard to see test results
	player1 = Deck()
	player2 = Deck()

	p1_score = 0
	p2_score = 0

	player1.shuffle()
	player2.shuffle()
	if not testing:
		print("\n*** BEGIN THE GAME ***\n")
	for i in range(52):
		p1_card = player1.pop_card()
		p2_card = player2.pop_card()
		if not testing:
			print("Player 1 plays", p1_card,"& Player 2 plays", p2_card)

		if p1_card.rank_num > p2_card.rank_num:
			if not testing:
				print("Player 1 wins a point!")
			p1_score += 1
		elif p1_card.rank_num < p2_card.rank_num:
			if not testing:
				print("Player 2 wins a point!")
			p2_score += 1
		else:
			if not testing:
				print("Tie. Next turn.")

	if p1_score > p2_score:
		return "Player1", p1_score, p2_score
	elif p2_score > p1_score:
		return "Player2", p1_score, p2_score
	else:
		return "Tie", p1_score, p2_score

if __name__ == "__main__":
	result = play_war_game()
	print("""\n\n******\nTOTAL SCORES:\nPlayer 1: {}\nPlayer 2: {}\n\n""".format(result[1],result[2]))
	if result[0] != "Tie":
		print(result[0], "wins")
	else:
		print("TIE!")


######### DO NOT CHANGE CODE ABOVE THIS LINE #########

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

#########
class Unit_Test_Cards(unittest.TestCase):

## Test that if you create a card with rank 12, its rank will be "Queen"
	def test_assert_Card_Queen(self):
		queen = Card(rank = 12)
		self.assertEqual(queen.rank, "Queen")
## Test that if you create a card with rank 1, its rank will be "Ace"
	def test_assert_Card_Ace(self):
		ace = Card(rank = 1)
		self.assertEqual(ace.rank, "Ace")
## Test that if you create a card instance with rank 3, its rank will be 3
	def test_assert_Card_3(self):
		three = Card(rank = 3)
		self.assertEqual(three.rank, 3)
## Test that if you create a card instance with suit 1, it will be suit "Clubs"
	def test_assert_Club(self):
		x = Card(suit = 1)
		self.assertEqual(x.suit, "Clubs")
## Test that if you create a card instance with suit 2, it will be suit "Hearts"
	def test_assert_Hearts(self):
		y = Card(suit= 2)
		self.assertEqual(y.suit, "Hearts")
## Test that if you create a card instance, it will have access to a variable suit_names that contains the list ["Diamonds","Clubs","Hearts","Spades"]
	def test_assert_suit_names(self):
		a = Card()
		self.assertEqual(a.suit_names, ["Diamonds", "Clubs", "Hearts", "Spades"])
## Test that if you invoke the __str__ method of a card instance that is created with suit=2, rank=7, it returns the string "7 of Hearts"
	def test_assert_str(self):
		b = Card(suit = 2, rank = 7)
		self.assertEqual(b.__str__(), "7 of Hearts")
## Test that if you create a deck instance, it will have 52 cards in its cards instance variable
	def test_assert_deck(self):
		l = Deck()
		self.assertEqual(len(l.cards), 52)
## Test that if you invoke the pop_card method on a deck, it will return a card instance.
	def test_assert_pop_card(self):
		m = Deck()
		p = Card()
		self.assertEqual(type(m.pop_card()), type(p))
## Test that the return value of the play_war_game function is a tuple with three elements, the first of which is a string. (This will probably require multiple test methods!)
	def test_assert_tuple(self):
		a = play_war_game(testing = True)
		b = "hi"
		self.assertEqual(len(a), 3)
		self.assertEqual(type(a[0]), type(b))
## Write at least 2 additional tests (not repeats of the above described tests). Make sure to include a descriptive message in these two so we can easily see what you are testing!
	# Test that if you create a card with rank 13, its rank will be "King"
	def test_assert_Card_King(self):
		king = Card(rank = 13)
		self.assertEqual(king.rank, "King")
	#This is a test to check if when you invoke the __str__ method of the Deck class, it returns the correct type, which is a string
	def test_assert_type_multiline_str(self):
		x = Deck()
		y = "hi"
		self.assertEqual(type(x.__str__()), type(y))
	#This is a test the play_war_game function, to see check that when the score of player 1 is equal to the score of player 2, the first item in the tuple is "Tie"
	def test_assert_tie(self):
		x = play_war_game(testing = True)
		self.assertEqual(x[1] == x[2], x[0] == "Tie")
	#This is a tests the return value of the play_war_game function to check that the second item in the tuple (player 1 score), is the correct type (an integer)
	def test_assert_type(self):
		x = play_war_game(testing = True)
		y = 1
		self.assertEqual(type(x[1]), type(y))
	# Test that if you create a card with rank 11, its rank will be "Jack"
	def test_assert_Card_Jack(self):
		jack = Card(rank = 11)
		self.assertEqual(jack.rank, "Jack")

##Run tests
x= Unit_Test_Cards()
x.test_assert_Card_Queen()
x.test_assert_Card_Ace()
x.test_assert_Card_3()


#############
## The following is a line to run all of the tests you include:
unittest.main(verbosity=2)
## verbosity 2 to see detail about the tests the code fails/passes/etc.
