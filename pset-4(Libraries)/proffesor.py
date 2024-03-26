import random
import sys

def main():
    while(True):
        level = getLevel()
        if(level > 3 or level < 0):
            level = getLevel()
        else:
            questions = 0
            trials = 3
            while(questions < 10 ):           
                firstOperand = generateInteger(level)
                secondOperand = generateInteger(level)
                userAnswer = input(f"{firstOperand} + {secondOperand}= ")
                correctAnswer = firstOperand + secondOperand
                try:
                    parsedAnswer = int(userAnswer)
                    while(trials > 0):
                        if(parsedAnswer != correctAnswer):
                            trials -=1
                            print("EEE")
                            userAnswer = input(f"{firstOperand} + {secondOperand}= ")
                        elif(trials == 0):
                            print(f"{firstOperand} + {secondOperand} = {correctAnswer}")
                        else:
                            continue
                except ValueError:
                    pass #Confirm if this step of logic should be implemented
            questions -=1
            continue

#Function used to capture the level user provides
def getLevel():
    while(True):
        try:
            userInput = int(input("Level: "))             
            return userInput
        except ValueError:
            pass
            
            
#Function to randomly generate an integer of LEVEL digits
def generateInteger(level):
    if(level == 1):
        operand = random.randint(0, 9)
    elif(level == 2):
        operand = random.randint(10, 99)
    else:
        operand = random.randint(100, 999)
    return operand












if __name__ == "__main__":
    main()