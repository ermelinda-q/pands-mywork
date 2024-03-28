# Programming and Scripting Week 08
# This program plots a histogram of the salaries using the output from numpyExists.py

# Based on Andrew Beatty's course lab - week 8
# Author: Ermelinda Qejvani

import numpy as np 
import matplotlib.pyplot as plt 

min_salary = 20000
max_salary = 80000
number_of_entries = 100

# the code below makes the program to give us the same numbers each time it runs.

np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, number_of_entries)

plt.hist(salaries)
plt.show()