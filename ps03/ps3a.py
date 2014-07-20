# 6.00 Problem Set 3A Solutions
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
#

# # PartA

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
	'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
	"""
	Returns a list of valid words. Words are strings of lowercase letters.
	
	Depending on the size of the word list, this function may
	take a while to finish.
	"""
	print "Loading word list from file..."
	# inFile: file
	inFile = open(WORDLIST_FILENAME, 'r', 0)
	# wordlist: list of strings
	wordlist = []
	for line in inFile:
		wordlist.append(line.strip().lower())
	print "	 ", len(wordlist), "words loaded."
	return wordlist

def get_frequency_dict(sequence):
	"""
	Returns a dictionary where the keys are elements of the sequence
	and the values are integer counts, for the number of times that
	an element is repeated in the sequence.

	sequence: string or list
	return: dictionary
	"""
	# freqs: dictionary (element_type -> int)
	freq = {}
	for x in sequence:
		freq[x] = freq.get(x,0) + 1
	return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n=7):
	"""
	Returns the score for a word. Assumes the word is a
	valid word.

	The score for a word is the sum of the points for letters
	in the word multiplied by the length of the word, plus 50
	points if all n letters are used on the first go.

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

	word: string (lowercase letters)
	returns: int >= 0
	"""
	score = 0
	for i in str(word):
		score += SCRABBLE_LETTER_VALUES[i]
	score *= len(word)
	if len(word) == n:
		score += 50
	else:
		score += 0
	return score

# print get_word_score('eight')
# print get_word_score('hello')
# print get_word_score('weed')
# print get_word_score('waybill')

def display_hand(hand):
	"""
	Displays the letters currently in the hand.

	For example:
	   display_hand({'a':1, 'x':2, 'l':3, 'e':1})
	Should print out something like:
	   a x x l l l e
	The order of the letters is unimportant.

	hand: dictionary (string -> int)
	"""
	for letter in hand.keys():
		for j in range(hand[letter]):
			 print letter,				# print all on the same line
	print								# print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n=7):
	"""
	Returns a random hand containing n lowercase letters.
	At least n/3 the letters in the hand should be VOWELS.

	Hands are represented as dictionaries. The keys are
	letters and the values are the number of times the
	particular letter is repeated in that hand.

	n: int >= 0
	returns: dictionary (string -> int)
	"""
	hand={}
	num_vowels = n / 3
	
	for i in range(num_vowels):
		x = VOWELS[random.randrange(0,len(VOWELS))]
		hand[x] = hand.get(x, 0) + 1
		
	for i in range(num_vowels, n):	  
		x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
		hand[x] = hand.get(x, 0) + 1
		
	return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
	"""
	Assumes that 'hand' has all the letters in word.
	In other words, this assumes that however many times
	a letter appears in 'word', 'hand' has at least as
	many of that letter in it. 

	Updates the hand: uses up the letters in the given word
	and returns the new hand, without those letters in it.

	Has no side effects: does not modify hand.

	word: string
	hand: dictionary (string -> int)	
	returns: dictionary (string -> int)
	"""
	new_hand = hand.copy()
	for i in word:
		new_hand[i] -= 1 
	return new_hand
	

# hand = deal_hand()
# print hand
# word = raw_input('>')
# hand = update_hand(hand, word)
# print hand
# print display_hand

# Problem #3: Test word validity
#
def is_valid_word(word, hand , word_list = load_words()):
	"""
	Returns True if word is in the word_list and is entirely
	composed of letters in the hand. Otherwise, returns False.
	Does not mutate hand or word_list.
	
	word: string
	hand: dictionary (string -> int)
	word_list: list of lowercase strings
	"""
	ans = True
	if word in word_list:
		for e in word:
			if e not in str(hand.keys()):
				ans = False
				break
	else:
		ans = False
	return ans

# hand = deal_hand()
# print hand
# word = raw_input('>')
# print is_valid_word(word, hand)

def calculate_handlen(hand):
	handlen = 0
	for v in hand.values():
		handlen += v
	return handlen

#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list = load_words() ):

	"""
	Allows the user to play the given hand, as follows:

	* The hand is displayed.
	
	* The user may input a word.

	* An invalid word is rejected, and a message is displayed asking
	  the user to choose another word.

	* When a valid word is entered, it uses up letters from the hand.

	* After every valid word: the score for that word is displayed,
	  the remaining letters in the hand are displayed, and the user
	  is asked to input another word.

	* The sum of the word scores is displayed when the hand finishes.

	* The hand finishes when there are no more unused letters.
	  The user can also finish playing the hand by inputing a single
	  period (the string '.') instead of a word.

	  hand: dictionary (string -> int)
	  word_list: list of lowercase strings
	  
	"""
	
	score = 0
	word = 0
	while word != '.':
		display_hand(hand)
		word = raw_input('Enter a valid word or "." to stop playing:')
		if word == '.':
			break
		word_value = is_valid_word(word, hand)
		while word_value == False:
			print "invalid word"
			word = raw_input('Enter a valid word or "." to stop playing:')
			word_value = is_valid_word(word, hand)
			if word == '.':
				break
		if word == '.':
			break
		score += get_word_score(word)
		hand = update_hand(hand, word)
		print "your new hand is:"
	print "Your score is %d" % score
	
# hand = deal_hand()
# play_hand(hand)
	
#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(a , word_list = load_words() ):
	"""
	Allow the user to play an arbitrary number of hands.

	* Asks the user to input 'n' or 'r' or 'e'.

	* If the user inputs 'n', let the user play a new (random) hand.
	  When done playing the hand, ask the 'n' or 'e' question again.

	* If the user inputs 'r', let the user play the last hand again.

	* If the user inputs 'e', exit the game.

	* If the user inputs anything else, ask them again.
	"""
	print """hit:
n for new hand"""
	global hand
	if a==1:
		print "r for new hand"
	print """e to exit"""
	inp=raw_input(">")
	if inp == "e":
		print "Bye!"
	else:
		if inp == "r" and a == 1:
			play_hand(hand)
		elif inp == "n":
			hand = deal_hand()
			play_hand(hand)
		play_game(1)
		
hand = deal_hand
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
	word_list = load_words()
	play_game(0, word_list)

