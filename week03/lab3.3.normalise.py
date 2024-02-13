# Programming and Scripting (coding with Python)

# Program Title: Working with String functions len(), strip(), lower()
# The program reads a string and strips any leading or trailing spaces.
# It also coverts all the letters to lower case.
# It then outputs the lengths of the original string and the normalised one

# Author: Ermelinda Qejvani

# 'raw_string' is a  variable representing user input
raw_string = input('Please enter a string: ')

# 'normalised_string'  is variable that will strip any any leading or trailing space
# it will also convert all letters to lower case
normalised_string = raw_string.strip().lower()

# 'length_of_raw_string' and 'length_of_normalised_string'will get the length of both strings
length_of_raw_string = len(raw_string)
length_of_normalised_string = len(normalised_string)

# Outputs:
print(f'The string you entered "{raw_string}" normalised is: {normalised_string}')
print(f' We reduced the input string from {length_of_raw_string} to {length_of_normalised_string} characters.')