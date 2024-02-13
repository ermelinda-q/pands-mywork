# Programming and Scripting Week 3
# This program prints out a random fruit.
# Author: Ermelinda Qejvani

import random

fruits = ['Apple', 'Orange', 'Banana', 'Pear', 'Grapes']

index  = random.randint(0, len(fruits)-1)

fruit = fruits[index]

print('A Random Fruit: {}'.format(fruit))
