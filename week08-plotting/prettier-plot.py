# Programming and Scripting Week 08
# this program uses the data from the salariesPlot and adds another list called ages
# that has the same number random values as salaries. We're making scatter plot of this data


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
ages = np.random.randint(low=21, high=65, size=number_of_entries)

plt.scatter(ages, salaries)     # this will be random
# plt.show()        # we need to show both diagrams in the same time

# adding x squared
x_points = np.array(range(1,101))
y_points = x_points * x_points # multiply x values by itself

plt.plot(x_points, y_points, color= 'r', label = "x squared")

plt.title("random plot")
plt.xlabel("salaries")
plt.ylabel("age")
plt.legend()
# plt.show()

# this line will change the axis
plt.savefig('prettier-plot.png')

