import random
import string

def error_params_none(param,msg):
    assert param !=None,msg 
def error_params_type(param,type_param,msg):
    assert type(param)!=type_param,msg 


class Words(object):

    def word_different_letters(self, available, secretWord):
        
        error_params_none(available,"available recebe nulo")
        error_params_type(available,string,"available não é String")
        error_params_none(secretWord,"secretWord recebe nulo")
        error_params_type(secretWord,string,"secretWord não é String")

        for letter in available:
            if letter in secretWord:
                available = available.replace(letter, '')
        different_words = 26-len(available)     
        return different_words

    def change_word(self, random_word, word_list):
        
        error_params_none(random_word,"random_word está recebendo nulo")
        error_params_type(random_word,string,"random_word não é String")
        error_params_none(word_list,"word_list recebe nulo")
        error_params_type(word_list,string,"word_list não é String")

        available = string.ascii_lowercase
        while self.word_different_letters(available, random_word) > 8:
            random_word = random.choice(word_list)
        else:
            return random_word

    
    def load_words(self):

        list_of_words = "palavras.txt"
        #print("Loading word list from file...")
        load_file = open(list_of_words, 'r')
        line = load_file.readline()
        word_list = str.split(line)
        print(len(word_list), "words loaded.")
        choice_word = random.choice(word_list)
        random_word = self.change_word(choice_word, word_list)
        return random_word

    def isWordGuessed(self, secretWord, lettersGuessed):
        
        error_params_none(secretWord,"secretWord está recebendo nulo")
        error_params_type(secretWord,string,"secretWord não é String")
        error_params_none(lettersGuessed,"lettersGuessed recebe nulo")
        error_params_type(lettersGuessed,string,"lettersGuessed não é String")        

        for letter in secretWord:
            if letter in lettersGuessed:
                pass
            else:
                return False
        return True


class Letters(object):

    def check_letter_word(self, secretWord, lettersGuessed, guessed):

        error_params_none(secretWord,"secretWord está recebendo nulo")
        error_params_type(secretWord,string,"secretWord não é String")
        error_params_none(lettersGuessed,"lettersGuessed recebe nulo")
        error_params_type(lettersGuessed,string,"lettersGuessed não é String")  
        error_params_none(guessed,"guessed recebe nulo")
        error_params_type(guessed,string,"guessed não é String") 

        for letter in secretWord:
            if letter in lettersGuessed:
                guessed += letter
            else:
                guessed += '_ '
        return guessed

    def count_letters(self, available, lettersGuessed):

        error_params_none(available,"available está recebendo nulo")
        error_params_type(available,string,"available não é String")
        error_params_none(lettersGuessed,"lettersGuessed recebe nulo")
        error_params_type(lettersGuessed,string,"lettersGuessed não é String")  


        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print('Available letters', available)

    def letter_guessed_again(self, guessed, lettersGuessed):

        error_params_none(lettersGuessed,"lettersGuessed recebe nulo")
        error_params_type(lettersGuessed,string,"lettersGuessed não é String")  
        error_params_none(guessed,"guessed recebe nulo")
        error_params_type(guessed,string,"guessed não é String") 


        guessed = self.check_letter_word(secretWord, lettersGuessed, guessed)
        print('Oops! You have already guessed that letter: ', guessed)

    def letter_good_guessed(self, letter, lettersGuessed):

        error_params_none(lettersGuessed,"lettersGuessed recebe nulo")
        error_params_type(lettersGuessed,string,"lettersGuessed não é String")  
        error_params_none(letter,"letter recebe nulo")
        error_params_type(letter,string,"letter não é String") 

        
        lettersGuessed.append(letter)
        guessed = ''
        guessed = self.check_letter_word(secretWord, lettersGuessed, guessed)
        print('Good Guess: ', guessed)

    def letter_wrong_guessed(self, letter, lettersGuessed):

        error_params_none(lettersGuessed,"lettersGuessed recebe nulo")
        error_params_type(lettersGuessed,string,"lettersGuessed não é String")  
        error_params_none(letter,"letter recebe nulo")
        error_params_type(letter,string,"letter não é String") 

        lettersGuessed.append(letter)
        guessed = ''
        guessed = self.check_letter_word(secretWord, lettersGuessed, guessed)
        print('Oops! That letter is not in my word: ',  guessed)


def hangman(secretWord):

    error_params_none(secretWord,"secretWord está recebendo nulo")
    error_params_type(secretWord,string,"secretWord não é String")
    
    available = string.ascii_lowercase
    guesses = 8
    lettersGuessed = []
    letters = Letters()
   # words = Words()
    jumpline='\n'

    print('Welcome to the game, Hangam!')
    print('I am thinking of a word that is', len(secretWord), ' letters long.')
    different_words = words.word_different_letters(available, secretWord)
    print('This word have ', different_words, 'different letters')
    print('-------------')

    while words.isWordGuessed(secretWord, lettersGuessed) == False and guesses > 0:
        print('You have ', guesses, 'guesses left.')
        letters.count_letters(available, lettersGuessed)

        letter = input('Please guess a letter: ')
        letter= letter.lower()
        if letter not in string.ascii_letters:
            print("This is not a letter,try again with letters")
        
        elif letter in jumpline:
            print("write something")

        elif letter in lettersGuessed:
            guessed = ''
            letters.letter_guessed_again(guessed, lettersGuessed)
        
        elif letter in secretWord and letter != None:
            letters.letter_good_guessed(letter, lettersGuessed)

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
secretWord = words.load_words().lower()
hangman(secretWord)
