# Coding Challenge 3, hangman.py
# Name: Tejvir Sohi
# Student No: 1926434

# Hangman Game

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import os.path
from string import ascii_lowercase

WORDLIST_FILENAME = "words.txt"

# Responses to in-game events
# Use the format function to fill in the spaces
responses = [
            "I am thinking of a word that is {0} letters long",
            "Congratulations, you won!",
            "Your total score for this game is: {0}",
            "Sorry, you ran out of guesses. The word was: {0}",
            "You have {0} guesses left.",
            "Available letters: {0}",
            "Good guess: {0}",
            "Oops! That letter is not in my word: {0}",
            "Oops! You've already guessed that letter: {0}",
        ]

def choose_random_word(all_words):
    """
    Chooses a random word from those available in the wordlist
    
    Args:
        all_words (list): list of available words (strings)
    
    Returns:
        a word from the wordlist at random
    """
    return random.choice(all_words)


# end of helper code
# -----------------------------------


def load_words():

    """
    Generate a list of valid words. Words are strings of lowercase letters.

    Returns:
        A list of valid words.
    """
    # TODO: Fill in your code here
    
    print("Loading word list from file...")
    dataList = []
    wordList = []
    loadingWords = True

    try:
        while(loadingWords):
            with open('words.txt', 'r') as file:
                data = file.read().replace('\n', '')
                data = data.split(" ")
                dataList.append(data)
                loadingWords = False

            for words in dataList[0]:
                wordList.append(words)

            print("Loading words is complete")
            print(f"Total number of words loaded: {len(wordList)}")
            return wordList
    except:
        print("There was an error loading wordlist from file")
        exit()
    
# Load the list of words into the variable wordlist
# Accessible from anywhere in the program
# TODO: uncomment the below line once
# you have implemented the load_words() function
wordlist = load_words()

def is_word_guessed(word, letters_guessed):
    """
    Determine whether the word has been guessed

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): the letters guessed so far
    
    Returns: 
        boolean, True if all the letters of word are in letters_guessed; False otherwise
    """
    # TODO: Fill in your the code here
    isWordGuessed = False
    word = set(word)
    letters_guessed = "".join(letters_guessed)
    isWordGuessed = set(letters_guessed) >= word
    isList = type(letters_guessed) is list

    if isList == False:
        letters_guessed = list(letters_guessed)
 
    if len(letters_guessed) == 1:
        for letter in letters_guessed:           
            if isWordGuessed == False:
                if letter in word:
                    isWordGuessed = True

    return isWordGuessed      
    

def get_guessed_word(word, letters_guessed):
    """
    Determines the current guessed word, with underscores

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): which letters have been guessed so far
    
    Returns: 
        string, comprised of letters, underscores (_), and spaces that represents which letters have been guessed so far.
    """
    # TODO: Fill in your code here
    
    guessedWord = ["_ "] *len(word)

    for letter in letters_guessed:

        for x in range(0, len(word)):
            if word[x] == letter:
                guessedWord[x] = letter           
    
    guessedWord = "".join(guessedWord)
    return guessedWord


def get_remaining_letters(letters_guessed):
    """
    Determine the letters that have not been guessed
    
    Args:
        letters_guessed: list (of strings), which letters have been guessed
    
    Returns: 
        String, comprised of letters that haven't been guessed yet.
    """
    # TODO: Fill in your code here

    alphabet = list(ascii_lowercase)
    
    for letter in letters_guessed:
        for character in alphabet:
            if letter == character:
                alphabet.remove(character)
                
    remainingLetters = "".join(alphabet)
    return remainingLetters

def get_score(name):
    
    #Asks the user if they want to view the leaderboard
    userMode = str(input("Would you like to view the leaderboard(yes/no): "))

    #Checks the users answers
    if "yes" in userMode:
        #Opens the file and reads it.
        scoresFile = open("scores.txt", "r")
        #Stores the contents of the file into a variable
        scoresFile = scoresFile.read()
        #Outputs the contents of the file.
        print(scoresFile)
        #Returns the user to main menu
        welcome_message()
    else:
        #Opens the file and reads it.
        scoresFile = open("scores.txt", "r")
        #Reads all the lines within the file
        scoresFile = scoresFile.readlines()
        scores = []

        #Loops through each line of the file
        for line in scoresFile:
            #Checks if the users name is on the line
            if name in line:
                #The follwing below splits the line every 2 characters and only appends the first 2 characters to a list
                n = 2
                score = [line[i:i+n] for i in range(0, len(line), n)]
                scores.append(score[0])
            elif not name in line:
                return 0

        #Checks what the highest score in the file is.
        highScore = max(scores)

        #Converst the highscore to an integer
        highScore = int(highScore)
        #Checks if the highscore is greater than 0
        if highScore > 0:
            return highScore
            

def save_score(name, score):

    #trys to do the following code. If it fails to complete this code, it catches the error.
    try:
        #Checks if the scores file exists.
        if os.path.isfile('scores.txt'):
            #Opens the file
            scoresFile = open("scores.txt", "r")
            #Reads all the lines within the file
            scoresFile = scoresFile.readlines()
            #Checks if the string is in the file. 
            if "Score\tName\n" in scoresFile:
                #Checks if the last line in the 
                if len(scoresFile[-1]) > 0:
                    #Opens the file
                    scoresFile = open("scores.txt", "a")
                    #Writes some information to the file
                    scoresFile.write(f"{score}\t{name}\n")
                    #Closes the file
                    scoresFile.close()
            else:
                #Opens the file
                scoresFile = open("scores.txt", "a")
                #Writes some information to the file
                scoresFile.write("Score\tName\n")
                scoresFile.write("------------\n")
                #Closes the file
                scoresFile.write(f"{score}\t{name}\n")
                scoresFile.close()
        else:
            #Writes the new file if it doesn't exist.
            scoresFile = open("scores.txt", "w+")
            #Writes some information to the file
            scoresFile.write("Score\tName\n")
            scoresFile.write("------------\n")
            scoresFile.write(f"{score}\t{name}\n")
            #Closes the file.
            scoresFile.close()      
    except Exception as e:
        #prints the error.
        print(e)


def welcome_message():
    print("--------------------------------------------")
    print("Welcome to Hangman Ultimate Edition")
    userMode = int(input("""Please selecet which mode you want to do using the number indicators
    1. Play Game
    2. View Leaderboard
    3. Quit\n:"""))
    
    #Choses a random word from words.txt
    word = choose_random_word(wordlist)
    
    #Checks which mode the user wishes to do.
    if userMode != 1 and userMode != 2 and userMode != 3:
        print("Invalid mode entered")
        print("Please enter a choice from the menu using a number.")
        welcome_message()
    elif userMode == 1:
        hangman(word)
    elif userMode == 2:
        name = str(input("Please enter your name: "))
        get_score(name)
    elif userMode == 3:
        print("Thanks for playing!")
        exit()

def hangman(word):
    """
    Runs an interactive game of Hangman.

    Args:
        word: string, the word to guess.
    """
    #user inputs their name. 
    name = str(input("Please enter your name: "))

    #The length of the random word is outputted.
    print("I am thinking of a word that is {0} letters long".format(len(word)))
    print("--------------------------------------------")
    print("_ "*len(word))
    # TODO: Fill in your code here
    
    #letters_guessed is a list that will contain all of the letters that the user has guessed.
    letters_guessed = []
    #userGuess is the length of the word plus 5
    userGuess = len(word) + 5
    #rounds begins at 1. There are 11 rounds in total.
    rounds = 1
    print(f"There are 11 rounds in total.")
    
    #is set to none to avoid errors
    guessedWord = None
    
    #The loop runs while rounds is less than or equal to 11.
    while rounds <= 11:
        #Informaition regarding rounds and guesses is outputted.
        print(f"Round: {rounds}")
        print(f"{responses[4]}".format(userGuess))
        #The user enters their guess.
        letter = str(input("Please enter your guess: "))
        letter = letter.lower()

        
        #Checks if the user has already guessed that letter. If not, then it is appended to the letters_guessed list.
        #If it is, the usr is told this, rounds is incremented and the loop skips the rest of the code.
        if letter in letters_guessed:
            print(f"{responses[8]}".format(guessedWord))  
            rounds += 1
            continue
        else:
            letters_guessed.append(letter)

        #Determines what the current guessed word is.    
        guessedWord = get_guessed_word(word, letters_guessed)
        #Determines if the word is guessed.
        wordGuessed = is_word_guessed(word, letters_guessed)
        
        #checks if the userGuess has decremented to 0. If so then user is returned to main menu.
        if userGuess == 0:
            print(f"{responses[3]}".format(word))
            welcome_message()
            
        else:        
            #Checks if the user ran out of rounds. If so, then the user is returned to the main menu.
            if rounds == 11:
                print(f"Sorry, you ran out of rounds. The secret word was: {word}")
                welcome_message()
            else:      
                #checks what the remaining letters are.
                remainingLetters = get_remaining_letters(letters_guessed)
                #Checks if there are not any underscores in the word. 
                if not "_ " in guessedWord:
                        #checks if word guesses if true.
                        if wordGuessed == True:
                            #The lines below determines what score the user acheived.
                            uniqueLetters = []
                            for letter in word:
                                if letter not in uniqueLetters:
                                    uniqueLetters.append(letter)
                            
                            score = userGuess * len(uniqueLetters)
                            #Gets the previous highscore from scores.txt if the user has one.
                            highScore = get_score(name) 

                            #checks if the users score is higher than their previous highscore.
                            if score > highScore :
                                print(f"{responses[1]}")
                                print(f"{responses[2]}".format(score))

                                #Determines output depnding on if the user had a prevoius highscore.
                                if highScore != 0:
                                    print(f"You just beat your previous highscore of {highScore}")
                                    updateHS = str(input("Would you like to save and update your new highscore(yes/no): "))
                                else:
                                    updateHS = str(input("Would you like to save your new highscore(yes/no): "))
                                
                                #Checks if the user wants to save their score
                                if "yes" in updateHS:
                                    #calls the method save score and saves it to a file.The user is then returned to the main menu.
                                    save_score(name, score)
                                    print("New highscore has been saved")
                                    welcome_message()
                                elif "no" in updateHS:
                                    #user is returned to the main menu if they do not wish to save their score.
                                    welcome_message()
                                else:
                                    #The score is saved anyay if an invalid input is entered. The user is returned to the main menu.
                                    print("Invalid input entered.\nProgram will save new highscore anyway")
                                    save_score(name, score)
                                    welcome_message()
                            else:    
                                #The same responses are outputted to the user as the true path to this if statment, but it is more tailored for someone who has played the game for the first time.
                                print(f"{responses[1]}")
                                print(f"{responses[2]}".format(score))
                                saveScore = str(input("Would you like to save your score?(yes/no) "))
                                
                                #Checks if the user wants to save their score.
                                if "yes" in saveScore:
                                    #calls the method save score and saves it to a file.The user is then returned to the main menu.
                                    save_score(name, score)
                                    print("Score has been saved")
                                    welcome_message()
                                if "no" in saveScore:
                                    #user is returned to the main menu if they do not wish to save their score.
                                    print("Thank you for playing Hangman Ultimate Edition")
                                    welcome_message()
                                else:
                                    #The score is saved anyay if an invalid input is entered. The user is returned to the main menu.
                                    print("Invalid input entered.\nProgram will save score anyway")
                                    save_score(name, score)
                                    welcome_message()
                                    

                #Checks if the letter the user guessed is empty or doesn't contain a letter.
                elif not letter in word or letter == "": 
                    #Determines what the current guessed word is.
                    guessedWord = get_guessed_word(word, letters_guessed)
                    print(f"{responses[7]}".format(guessedWord))
                    print(f"{responses[5]}".format(remainingLetters))
                    rounds += 1
                #Checks if the user has used a vowel
                    if letter in ["a","e","i","o","u"] :
                        userGuess -= 2
                    else:
                        userGuess -= 1               
                #Checks if the user has used a vowel
                elif letter in ["a","e","i","o","u"] :
                    #Determines what the current guessed word is.
                    guessedWord = get_guessed_word(word, letters_guessed)
                    #prints the output to the user 
                    print(f"{responses[6]}".format(guessedWord))
                    print(f"{responses[5]}".format(remainingLetters))
                    print("--------------------------------------------")
                    userGuess -= 2
                    rounds += 1
                else:
                    #Determines what the current guessed word is.
                    guessedWord = get_guessed_word(word, letters_guessed)
                    #prints the output to the user
                    print(f"{responses[6]}".format(guessedWord))
                    print(f"{responses[5]}".format(remainingLetters))
                    print("--------------------------------------------")
                    userGuess -= 1
                    rounds += 1                  
                    

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the last lines to test
# (hint: you might want to pick your own
# word while you're doing your own testing)


# -----------------------------------

# Driver function for the program
if __name__ == "__main__":
    # Uncomment the line below once you have finished testing.
    

    # Uncomment the line below once you have implemented the hangman function.
    welcome_message()
