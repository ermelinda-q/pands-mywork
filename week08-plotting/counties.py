# Programming and Scripting week 08
# This program had a list of counties, make some counties appear more than others
# Creates a pie chart of the counties.

# Based on Andrew Beatty's week 8 lab

# Author: Ermelinda Qejvani

import numpy as np 
import matplotlib.pyplot as plt 

# creating the array of occurrences
possible_counties = ['Mayo', 'Galway', 'Roscommon', 'DirtyDublin', 'Donegal']

# Pick 100 randomly from possible counties with the frequence set in p
counties = np.random.choice(
    possible_counties,
    p=[0.1, 0.3, 0.2, 0.12, 0.28],
    size=(100)
)
# right now we need the number of accuurences of each county
# this returns a tuple of the unique values and how many times they appear
unique, counts = np.unique(counties, return_counts=True)
# we can now put this into a pie plot
# plt.pie(counts, labels=unique)

# using bar charts
plt.bar(unique, counts)

plt.show()


