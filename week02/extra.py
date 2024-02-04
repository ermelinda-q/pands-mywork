# This program is asking for your name, age,entering two numbers and making some maths operation with the numbers
# Week 02 - Programming with Python
# Author: Ermelinda Qejvani

import time # calling python time module to use in this program

name = input('Enter your name: ') # creating some variables
age = input('Enter your age: ')


print (f'Hello {name}, \t your age is {age}.')
time.sleep(1)               # just giving a second to the user to read the full sentence :)

#second part, some maths calculations

question = input('Do you like maths? ')
if question == str('yes' or 'Yes') :

    numberOne = int(input('Write a number: '))
    numberTwo = int(input('Write another number: '))
    numberMultiply = numberOne * numberTwo
    numberDivide = numberOne / numberTwo
    numberAdd = numberOne + numberTwo
    numberSubtract = numberOne - numberTwo
    numberCompare = numberOne ==numberTwo

    time.sleep(1)
    print(f'{numberOne} plus {numberTwo} is {numberAdd}')
    time.sleep(1)
    print(f'{numberOne} minus {numberTwo} is {numberSubtract}')
    time.sleep(1)
    print(f'{numberOne} multiply {numberTwo} is {numberMultiply}')
    time.sleep(1)
    print(f'{numberOne} devided by {numberTwo} is {numberDivide}')
    time.sleep(1)
    print(f'{numberOne} = {numberTwo} is {numberCompare}')
    time.sleep(1)
    print('Goodbye ' + name)

elif  question != 'yes' or 'Yes':   
    print('Goodbye ' + name)






