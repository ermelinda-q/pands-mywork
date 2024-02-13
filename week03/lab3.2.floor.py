# Programming and Scripting (coding with Python)

# Program Title: Flooring down a number
# The program takes a number and rounds it to the nearest number DOWN

# Author: Ermelinda Qejvani

# First we import/call a built in module(math module) from the library

import math

# create a variable 'numberTofloor' as a float number entered as a user input

numberTofloor = float(input('Enter a float number: '))

# create a variable 'flooredNumber' which will call the math.floor function from the 'math' module
# to round the number to the nearest number down

flooredNumber = math.floor(numberTofloor)

# using print function to output a message: 
# 'numberTofloor'(value) floored is 'flooredNumber'

print('{} floored is {}'.format(numberTofloor, flooredNumber))
