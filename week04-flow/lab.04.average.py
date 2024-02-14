# Programming and Scripting Week 4
# Program Title: Reading a list.
# This program keeps reading numbers until the user enters a 0. 
# The program should then print out each of the numbers entered and their average.

# Author: Ermelinda Qejvani

numbers = [] # creating the list of numbers

number = int(input("Enter number (0 to quit): ")) # first number 

while number != 0:  # checking if it is 0 while looping
    numbers.append(number) # adding number to the list 'numbers'

    number = int(input("Enter another number (0 to quit): ")) # reading next number and check if 0

for value in numbers:
    print (value)

# average as a float
average = float(sum(numbers)) / len(numbers)
print(f"The average of numbers entered is {average}")

