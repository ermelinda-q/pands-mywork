# Programming and Scripting Week 4
# This program reads in a students percentage and
# prints out the corresponding grade

# Author: Ermelinda Qejvani

percentage = float(input('Enter the percentage: '))
round_percentage = round(percentage)

# print (percentage)

if round_percentage < 0 or percentage > 100: # checking that is in the range we need 0-100
    print('Please enter a number between 0 and 100')
elif round_percentage < 40: # percentage > 0 and < 40
    print('Fail')
elif round_percentage < 50: # percentage between 40 and 50
        print('Pass')
elif round_percentage < 60: # between 50 and 60
        print('Merit1')
elif round_percentage < 70: # between 60 and 70
        print('Merit2')
else: # between 70 and 100
        print('Distinction')

