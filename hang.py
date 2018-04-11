import random
import string


#load the file words in 
def loadWords():
   
    WORDLIST_FILENAME = "palavras.txt" #put the wordlist inside the method 
    print( "Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')  #question to teacher
    line = inFile.readline()
    wordlist = str.split(line)#ver se n se pode mudar line
    print (len(wordlist), "words loaded.")
    random_word=random.choice(wordlist)
    random_word=change_word(random_word,wordlist)
   
    return random_word
#change the word if the word has more than 8 different letters
def change_word(random_word,wordlist):
    available = string.ascii_lowercase
    while count_different_letters(available,random_word)>8:
        random_word=random.choice(wordlist)
    else:
        return random_word
#check if the letters was guessed           
def check_letter_word(secretWord,lettersGuessed,guessed):

    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '
    return guessed
#count how many different letters has in a word
def count_different_letters(available,secretWord):
    for letter in available:
        if letter in secretWord:
            available = available.replace(letter, '')
            
    different_words=26-len(available)
    return different_words
#count how many letters has in a word
def count_letters(available,lettersGuessed):
  
    for letter in available:
        if letter in lettersGuessed:
            available = available.replace(letter, '')
        
    print ('Available letters', available)
#
def isWordGuessed(secretWord, lettersGuessed):
  
    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True
#letter guessed more than
def letter_guessed_again(guessed,lettersGuessed):

    guessed=check_letter_word(secretWord,lettersGuessed,guessed)
    print('Oops! You have already guessed that letter: ', guessed)
   
def letter_good_guessed(letter,lettersGuessed):
    lettersGuessed.append(letter)   
    guessed = ''
    
    guessed=check_letter_word(secretWord,lettersGuessed,guessed)
    print( 'Good Guess: ', guessed)

def letter_wrong_guessed(letter,lettersGuessed):
    
    lettersGuessed.append(letter)
   
    guessed = ''
   
    guessed=check_letter_word(secretWord,lettersGuessed,guessed)
    print ('Oops! That letter is not in my word: ',  guessed)
    

def hangman(secretWord):
    available = string.ascii_lowercase
    guesses = 8
    lettersGuessed = []
    
    print( 'Welcome to the game, Hangam!')
    print('I am thinking of a word that is', len(secretWord), ' letters long.')
    print ('-------------')
    
    
    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:#tentar arrumar com outra variavel ao invés de passar o método
        print ('You have ', guesses, 'guesses left.')

        count_letters(available,lettersGuessed)

        letter = input('Please guess a letter: ')

        if letter in lettersGuessed:
            guessed = ''
            letter_guessed_again(guessed,lettersGuessed)
        elif letter =="tip":
            different_words = count_different_letters(available,secretWord)
            print ('This word have ',different_words,'different letters')
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
