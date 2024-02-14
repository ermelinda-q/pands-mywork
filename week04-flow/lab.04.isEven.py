# Programming and Scripting Week 4
# This program asks the user to enter a number, and then will tell if number is even or odd.

# Author: Ermelinda Qejvani

number = int(input('Enter an interger: '))

if (number % 2) == 0:  # checking if number divided by 2 gives or not a reminder (even or odd)
    print(f'{number} is an even number')

else: 
    print(f'{number} is an odd number')

    