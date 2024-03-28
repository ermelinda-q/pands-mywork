# Programming ad Scripting Week 08
# this program plots the function y = x power of 2

# Based on Andrew Beatty's lab - week 8
# Author: ermelinda Qejvani

import matplotlib.pyplot as plt 
import numpy as np 

x_points = np.array(range(1,101))
y_points = x_points * x_points # multiplying each x entry by itself

plt.plot(x_points, y_points)
plt.show()