# Programming and Scripting Week 4
# Program Title: Lists & random library
# This program generates 10 random numbers, prints them out
# then prints out the top 3

# Author: Ermelinda Qejvani

import random # calling the build in random module

# main variables
howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

numbers = []    # list created named numbers

for i in range(0,howMany):
    numbers.append(random.randint(rangeFrom,rangeTo))
print(f"{howMany} random numbers\t {numbers}")

topOnes = numbers.copy()  # making a copy of original list
topOnes.sort(reverse=True)
print(f"The top {topHowMany} are \t\t {topOnes[0:topHowMany]}")



