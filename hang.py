import random
import string
import re


class Words(object):
    def word_different_letters(self, available, secretWord):

        for letter in available:
            if letter in secretWord:
                available = available.replace(letter, '')

        different_words = 26-len(available)
        return different_words

    def change_word(self, random_word, word_list):

        available = string.ascii_lowercase
        while self.word_different_letters(available, random_word) > 8:
            random_word = random.choice(word_list)
        else:
            return random_word

    # load the file words in
    def loadWords(self):

        list_of_words = "palavras.txt"
        print("Loading word list from file...")
        load_file = open(list_of_words, 'r')
        line = load_file.readline()
        word_list = str.split(line)
        print(len(word_list), "words loaded.")
        random_word = random.choice(word_list)
        random_word = self.change_word(random_word, word_list)
        return random_word

    def isWordGuessed(self, secretWord, lettersGuessed):

        for letter in secretWord:
            if letter in lettersGuessed:
                pass
            else:
                return False
        return True


class Letters(object):

    def check_letter_word(self, secretWord, lettersGuessed, guessed):

        for letter in secretWord:
            if letter in lettersGuessed:
                guessed += letter
            else:
                guessed += '_ '
        return guessed
   

    def count_letters(self, available, lettersGuessed):

        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print('Available letters', available)

    def letter_guessed_again(self, guessed, lettersGuessed):

        guessed = self.check_letter_word(secretWord, lettersGuessed, guessed)
        print('Oops! You have already guessed that letter: ', guessed)

    def letter_good_guessed(self, letter, lettersGuessed):
        lettersGuessed.append(letter)
        guessed = ''

        guessed = self.check_letter_word(secretWord, lettersGuessed, guessed)
        print('Good Guess: ', guessed)

    def letter_wrong_guessed(self, letter, lettersGuessed):

        lettersGuessed.append(letter)

        guessed = ''

        guessed = self.check_letter_word(secretWord, lettersGuessed, guessed)
        print('Oops! That letter is not in my word: ',  guessed)

   # def validation_alphabetic_letter(self,lettersGuessed):
        


def hangman(secretWord):
    available = string.ascii_lowercase
    guesses = 8
    lettersGuessed = []
    letters = Letters()
    words = Words()
    alphabetic_letters='abcdefghijklmnopqrstuvxyz'

    print('Welcome to the game, Hangam!')
    print('I am thinking of a word that is', len(secretWord), ' letters long.')
    different_words = words.word_different_letters(available, secretWord)
    print('This word have ', different_words, 'different letters')
    print('-------------')

   
    while words.isWordGuessed(secretWord, lettersGuessed) == False and guesses > 0:
        print('You have ', guesses, 'guesses left.')

        letters.count_letters(available, lettersGuessed)

        letter = input('Please guess a letter: ')

        if letter in lettersGuessed:
            guessed = ''
            letters.letter_guessed_again(guessed, lettersGuessed)
        elif letter in secretWord:
            letters.letter_good_guessed(letter, lettersGuessed)
                      
        elif letter not in alphabetic_letters:
            print("this is not a letter,try again with letters")   
        else:
            guesses -= 1
            letters.letter_wrong_guessed(letter, lettersGuessed)

        print('------------')

    else:
        if words.isWordGuessed(secretWord, lettersGuessed) == True:
            print('Congratulations, you won!')
        else:
            print('Sorry, you ran out of guesses. The word was ', secretWord, '.')


words = Words()
secretWord = words.loadWords().lower()
hangman(secretWord)
