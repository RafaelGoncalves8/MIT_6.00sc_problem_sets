from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list = load_words()):
	"""
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

	hand: dictionary (string -> int)
	word_list: list (string)
	"""
	ans = None
	for e in range(8):
		anagrams = get_perms(hand, e)
		for word in anagrams:
			if is_valid_word(word, hand):
				ans = word
				break
	return ans

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list = load_words()):
	"""
	 Allows the computer to play the given hand, as follows:

	 * The hand is displayed.

	 * The computer chooses a word using comp_choose_words(hand, word_dict).

	 * After every valid word: the score for that word is displayed, 
	   the remaining letters in the hand are displayed, and the computer 
	   chooses another word.

	 * The sum of the word scores is displayed when the hand finishes.

	 * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

	 hand: dictionary (string -> int)
	 word_list: list (string)
	"""
	score = 0
	word = 0
	while word != None:
		display_hand(hand)
		word = comp_choose_word(hand, word_list)
		word_value = is_valid_word(word, hand)
		if word_value == False:
			word = None
		print word
		if word == None:
			break
		score += get_word_score(word)
		hand = update_hand(hand, word)
	print "Computer's score: %d" % score
	
# comp_play_hand(deal_hand(),load_words())
	
#
# Problem #6C: Playing a game
#
#
def play_game(a, x, word_list = load_words()):
	"""Allow the user to play an arbitrary number of hands.

	1) Asks the user to input 'n' or 'r' or 'e'.
	* If the user inputs 'n', play a new (random) hand.
	* If the user inputs 'r', play the last hand again.
	* If the user inputs 'e', exit the game.
	* If the user inputs anything else, ask them again.

	2) Ask the user to input a 'u' or a 'c'.
	* If the user inputs 'u', let the user play the game as before using play_hand.
	* If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
	* If the user inputs anything else, ask them again.

	3) After the computer or user has played the hand, repeat from step 1

	word_list: list (string)
	"""
	global hand
	inp = ' '
	if x == 'u':
		print """hit:
n for new hand"""
		if a==1:
			print "r for play last hand again hand"
		print """e to exit"""
		inp=raw_input(">")
	if a == 0 and inp != 'e':
		x = raw_input("Who will start? 'u' for you and 'c' for computer \n>")
	if inp == "e":
		print "Bye!"
	else:
		if x == 'u':
			if inp == "r" and a == 1:
				play_hand(hand)
			elif inp == "n":
				hand = deal_hand()
				play_hand(hand)
			
			x = 'c'
		else:
			comp_play_hand(hand)
			x = 'u'
		play_game(1, x, )
		
hand = deal_hand()

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
	word_list = load_words()
	play_game(0, 'u', word_list)


	
