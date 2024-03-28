# Programming and Scripting
# Week 8 - Plotting
# This program makes a list, called 'salaries', that has 10 random numbers between 20000-80000.

# Based on Andrew Beatty's 'Lab Toppic 08-plotting'
# Author: Ermelinda Qejvani

import numpy as np 
# variables for our values
min_salary = 20000
max_salary = 80000
number_of_entries = 10
np.random.seed(1)       # printing the same values each time the program runs
salaries = np.random.randint(min_salary, max_salary, number_of_entries)
#printing the same numbers

print(salaries)

salaries_plus = salaries + 5000     # adding 5000 to each value
print(salaries_plus)

# modify the program to increase all salaries by 5% (store in another array)

# we can multiply
salaries_mul = salaries * 1.05 # add 5% by multiplying by 1.05
print(salaries_mul)

# this is a float array, here we convert it to an int array.

new_salaries = salaries_mul.astype(int)
print(new_salaries)