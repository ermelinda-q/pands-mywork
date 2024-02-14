# Programming and Scripting Week 4
# This program tells the user to enter(guess) a number telling the user if their guess
# is too high or too low each time they guess.

# Author: Ermelinda Qejvani

numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else:
        print("too high")
    guess = int(input("Please guess again: "))

print("Well done! Yes the number was ", numberToGuess)
