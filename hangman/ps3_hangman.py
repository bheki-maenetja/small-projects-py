# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    return ''.join([i if i in lettersGuessed else '_' for i in secretWord])

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    return ''.join([i for i in string.ascii_lowercase if i not in lettersGuessed])

def get_string(min_length, max_length, input_prompt, accept_values=None):
  while True:
    try:
      string = input(f"{input_prompt}: ").lower()
      if accept_values != None:
        if string not in accept_values: raise ValueError
      if len(string) > max_length or len(string) < min_length: raise ValueError
    except ValueError:
      pass
    else:
      break
  
  return string

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    availableLetters = []
    numGuesses = 8

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word", len(secretWord), "letters long.\n-------------")

    while True:
      # Check if loop should be broken
      if numGuesses == 0:
        print("Sorry, you ran out of guesses. The word was", secretWord,".")
        break
      elif isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
        break

      # Update
      availableLetters = getAvailableLetters(lettersGuessed)
      # User Input
      print("You have", numGuesses, "guesses left.")
      print("Available letters:", availableLetters)
      player_guess = get_string(1,1,"Please enter a letter", accept_values=string.ascii_lowercase)

      if player_guess in lettersGuessed:
        print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed), "\n-------------")
      elif player_guess in secretWord:
        lettersGuessed.append(player_guess)
        print("Good guess:", getGuessedWord(secretWord, lettersGuessed),"\n-------------")
      else:
        lettersGuessed.append(player_guess)
        print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed), "\n-------------")
        numGuesses -= 1

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman("else")
