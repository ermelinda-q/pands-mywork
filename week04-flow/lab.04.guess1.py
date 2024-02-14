# Programming and Scripting Week 4
# This program prompts the user to guess a number and runs until the user gets the right number

# Author: Ermelinda Qejvani

numberToGuess = 30 # this is the number user should guess

guess = int(input("Please guess the number: ")) # guess- a variable(int) entered from user

# while loop - run until number 30 is entered from user

while guess != numberToGuess:  # while number is not 30('guess')
    print("Wrong")
    guess = int(input("Please guess again: ")) # guess value changed to users new input
    
print ("Well done! Yes the number was ", numberToGuess)
