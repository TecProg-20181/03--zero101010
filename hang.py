import random
import string
import logging

def apply_asserts(param,type_param,msg_none,msg_type):
    
    assert param !=None,msg_none 
    assert type(param)!=type_param,msg_type 

class Words(object):

    def word_different_letters(self, available, secretWord):
        
        apply_asserts(available,string,"available recebe nulo","available não é String")
        apply_asserts(secretWord,string,"secretWord recebe nulo","secretWord não é String")
       
        for letter in available:
            if letter in secretWord:
                available = available.replace(letter, '')
        different_words = 26-len(available)     
        return different_words

    def change_word(self, random_word, word_list):
        
        apply_asserts(random_word,string,"available recebe nulo","random_word não é String")
        apply_asserts(word_list,string,"word_list recebe nulo","word_list não é String")

        available = string.ascii_lowercase
        while self.word_different_letters(available, random_word) > 8:
            random_word = random.choice(word_list)
        else:
            return random_word

    def load_words(self):

        list_of_words = "palavras.txt"
        print("Loading word list from file...")
        load_file = open(list_of_words, 'r')
        line = load_file.readline()
        word_list = str.split(line)
        print(len(word_list), "words loaded.")
        choice_word = random.choice(word_list)
        random_word = self.change_word(choice_word, word_list)
        return random_word

    def isWordGuessed(self, secretWord, lettersGuessed):

        apply_asserts(secretWord,string,"secretWord recebe nulo","secretWord não é String")
        apply_asserts(lettersGuessed,string,"lettersGuessed recebe nulo","lettersGuessed não é String")
             
        for letter in secretWord:
            if letter in lettersGuessed:
                pass
            else:
                return False
        return True


class Letters(object):

    def check_letter_word(self, secretWord, lettersGuessed, guessed):
      
        apply_asserts(secretWord,string,"secretWord recebe nulo","secretWord não é String")
        apply_asserts(lettersGuessed,string,"lettersGuessed recebe nulo","lettersGuessed não é String")
        apply_asserts(guessed,string,"guessed recebe nulo","guessed não é String")

        for letter in secretWord:
            if letter in lettersGuessed:
                guessed += letter
            else:
                guessed += '_ '
        return guessed

    def count_letters(self, available, lettersGuessed):

        apply_asserts(available,string,"available recebe nulo","available não é String")
        apply_asserts(lettersGuessed,string,"lettersGuessed recebe nulo","lettersGuessed não é String")  

        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print('Available letters', available)

    def letter_guessed_again(self, guessed, lettersGuessed):

        apply_asserts(lettersGuessed,string,"lettersGuessed recebe nulo","lettersGuessed não é String")  
        apply_asserts(guessed,string,"guessed recebe nulo","guessed não é String")

        guessed = self.check_letter_word(secretWord, lettersGuessed, guessed)
        print('Oops! You have already guessed that letter: ', guessed)

    def letter_good_guessed(self, letter, lettersGuessed):

        apply_asserts(lettersGuessed,string,"lettersGuessed recebe nulo","lettersGuessed não é String")  
        apply_asserts(letter,string,"letter recebe nulo","letter não é String")

        lettersGuessed.append(letter)
        guessed = ''
        guessed = self.check_letter_word(secretWord, lettersGuessed, guessed)
        print('Good Guess: ', guessed)

    def letter_wrong_guessed(self, letter, lettersGuessed):
        
        apply_asserts(lettersGuessed,string,"lettersGuessed recebe nulo","lettersGuessed não é String")  
        apply_asserts(letter,string,"letter recebe nulo","letter não é String")

        lettersGuessed.append(letter)
        guessed = ''
        guessed = self.check_letter_word(secretWord, lettersGuessed, guessed)
        print('Oops! That letter is not in my word: ',  guessed)


def hangman(secretWord):

    logging.basicConfig(filename='filelog.log',level=logging.DEBUG)
    apply_asserts(secretWord,string,"secretWord recebe nulo","secretWord não é String")
    
    available = string.ascii_lowercase
    guesses = 8
    lettersGuessed = []
    letters = Letters()
    jumpline='\n'
    
    print('Welcome to the game, Hangam!')
    print('I am thinking of a word that is', len(secretWord), ' letters long.')

    logging.debug("start")
    
    different_words = words.word_different_letters(available, secretWord)
    print('This word have ', different_words, 'different letters')
    print('-------------')

    logging.debug("read the quantity of words in the file")

    while words.isWordGuessed(secretWord, lettersGuessed) == False and guesses > 0:
        print('You have ', guesses, 'guesses left.')
        letters.count_letters(available, lettersGuessed)

        letter = input('Please guess a letter: ')
        letter= letter.lower()
        
        logging.debug("Enter with the letter ")
        
        if letter not in string.ascii_letters:
            print("This is not a letter,try again with letters")
            logging.debug("Enter with something that ins't a letter ")
        
        elif letter in jumpline:
            print("write something")
            logging.debug("The letter is Null")
        
        elif letter in lettersGuessed:
            guessed = ''
            letters.letter_guessed_again(guessed, lettersGuessed)
            logging.debug("The letter was written")
        
        elif letter in secretWord and letter != None:
            letters.letter_good_guessed(letter, lettersGuessed)
            logging.debug("The letter is in the word")
        
        else:
            guesses -= 1
            letters.letter_wrong_guessed(letter, lettersGuessed)
            logging.debug("The letter isn't in the word")
        print('------------')

    else:
        if words.isWordGuessed(secretWord, lettersGuessed) == True:
            print('Congratulations, you won!')
            logging.debug("The player won")
        
        else:
            print('Sorry, you ran out of guesses. The word was ', secretWord, '.')
            logging.debug("The player lose ")
    
    logging.debug("finish the program")

words = Words()
secretWord = words.load_words().lower()
hangman(secretWord)
