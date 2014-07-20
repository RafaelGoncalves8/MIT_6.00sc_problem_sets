# A Wordgame: Hangman
=================================

import random
import string

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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program

def partial_word(word, guessed_letters):
    """
    Return the secret_word in user-visible format, with underscores used
    to replace characters that have not yet been guessed.
    """
    result = ''
    for letter in word:
        if letter in guessed_letters:
            result = result + letter
        else:
            result = result + '_'
    return result

def Hangman(guesses = 20):
	wordlist = load_words()
	word = choose_word(wordlist)
	print "\n\tWelcome to the game, Hangman!", "\n", "="*45, "\n"
	print "I'm thinking of a word with %d letters" % len(word)
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	guessing_word = []
	guessed_letters = []
	win = 0
	for j in range(len(word)):
		guessing_word.append('_')
	while win == 0 and guesses > 0:
		print guessing_word
		print "%d guesses left" % guesses
		print "Avaiable letters:" + ''.join(letters)
		print "Guessed letters:", guessed_letters
		guess = raw_input('Please guess a letter:\n>>')
		if guess in word and guess not in guessed_letters:
			print 'Good guess!'
			letters.remove(guess)
			guessed_letters += guess
			print partial_word(word, guessed_letters)
		elif guess in guessed_letters:
			print 'You already chosen that letter, try again'
		else:
			print "Oops! This letter insn't in the word."
			guesses -= 1
			letters.remove(guess)
			guessed_letters.append(guess)
		if word == partial_word(word, guessed_letters):
			win = 1
			break
	if win == 1:
		print "You won! Tap 1 to try again or 0 if you want to quit."
		a = int(raw_input('>>'))
		if a == 1:
			Hangman()
	else:
		print "You loose, tap 1 to try again or 0 if you want to quit."
		a = int(raw_input('>>'))
		if a == 1:
			Hangman()
		

Hangman()