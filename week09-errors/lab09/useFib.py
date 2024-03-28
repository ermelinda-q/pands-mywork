# Programming and Scripting - Week 9 lab
# This program calls a function in a module called 'myFunctions' 
# The program prompts the user for a number and prints out
# the fibonacci sequence of that many numbers
# Based on week 9 lectures by Andrew Beatty
# Author: Ermelinda Qejvani

import myFunctions

n_times = int(input('how many: '))
print(myFunctions.fibonacci(n_times))