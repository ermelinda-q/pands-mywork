# Programming and Scripting (coding with Python)

#  Give the absolute value of a number

# Author: Ermelinda Qejvani

# 

# variable 'number' set as float number. Asking user to enter a number
number = float(input('Enter a number: '))

# variable absoluteValue will use abs() function to return the 
# absolute value of number entered (variable 'number')
absoluteValue = abs(number)

# Output will be: The absolute value of (number entered) is (absolute value of number after abs() fuction is called)
print('The absolute value of {} is {}'.format(number,absoluteValue))
