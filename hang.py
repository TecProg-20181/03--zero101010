import random
import string

#load the file words in 
def loadWords():
    WORDLIST_FILENAME = "words.txt" #put the wordlist inside the method 
    print( "Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')  #perguntar mudança
    line = inFile.readline()
    wordlist = str.split(line)#ver se n se pode mudar line
    print ("  ", len(wordlist), "words loaded.")
    return random.choice(wordlist)

def count_diferent_letters(available,secretWord):
    for letter in available:
        if letter in secretWord:
            available = available.replace(letter, '')
    print ('This word have ',26-len(available),'diferent letters')

def count_letters(available,lettersGuessed):
  
    for letter in available:
        if letter in lettersGuessed:
            available = available.replace(letter, '')
        
    print ('Available letters', available)

def isWordGuessed(secretWord, lettersGuessed):
  
    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def letter_guessed_again(letter,guessed,lettersGuessed):

    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '
    print('Oops! You have already guessed that letter: ', guessed)
   
def letter_good_guessed(letter,lettersGuessed):
    lettersGuessed.append(letter)   
    guessed = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '

    print( 'Good Guess: ', guessed)

def letter_wrong_guessed(letter,lettersGuessed):
    
    lettersGuessed.append(letter)

    guessed = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '

    print ('Oops! That letter is not in my word: ',  guessed)
    

def hangman(secretWord):
    available = string.ascii_lowercase
    guesses = 8
    lettersGuessed = []
    
    print( 'Welcome to the game, Hangam!')
    print('I am thinking of a word that is', len(secretWord), ' letters long.')
    count_diferent_letters(available,secretWord)
    print ('-------------')
    
    
    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:#tentar arrumar com outra variavel ao invés de passar o método
        print ('You have ', guesses, 'guesses left.')

       
        
        count_letters(available,lettersGuessed)

        letter = input('Please guess a letter: ')
        if letter in lettersGuessed:
            guessed = ''
            letter_guessed_again(letter,guessed,lettersGuessed)
            
          
        elif letter in secretWord:
            letter_good_guessed(letter,lettersGuessed)
          
        else:
            guesses -=1
            letter_wrong_guessed(letter,lettersGuessed)
            
        print ('------------')
            
    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print ('Congratulations, you won!')
        else:
            print ('Sorry, you ran out of guesses. The word was ', secretWord, '.')




secretWord = loadWords().lower()
hangman(secretWord)
