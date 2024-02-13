# Programming and Scripting Week 3
# This program reads in two numbers, divides them and gives the integer result & remainder
# Author: Ermelinda Qejvani

x = int(input('Enter first number: '))
y = int(input('Enter the number you want to divide by: '))
answer = int(x//y)
remainder = x%y

print('{} divided by {} is {} with remainder {}'.format(x, y, answer, remainder))
