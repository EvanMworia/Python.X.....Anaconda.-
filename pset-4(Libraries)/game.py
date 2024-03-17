import random
import sys
#function used in getting the integer
def getInteger():
    while(True):
        try:
            userInput = int(input("Level: "))
            return userInput
        except ValueError:
            pass
            
            
#functon used in getting the Guess
def getGuess():
    while(True):
        try:
            userInput = int(input("Guess: "))
            return userInput
        except ValueError:
            pass
level = getInteger()
guess = getGuess()
randomNumber = random.randint(1, level)

while(True):
    if(guess == randomNumber):
        
        sys.exit("Just Right!")
        
    elif(guess > randomNumber):
        #if too large then reprompt
        print("Too Large!")
        guess = getGuess()
    elif(guess < randomNumber):
        #if too small then reprompt
        print("Too Small!")
        guess = getGuess()





