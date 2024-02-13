# Programming and Scripting Week 3
# Extra lab - fixing and error
# Author: Ermelinda Qejvani

# Question 6: Why does this expression cause an error?

# message = 'I have eaten ' + 99 + 'burritos.'
# print(message)

# Answer: program is expecting to read a string variable not a number

# Different ways of writing the code: this will print the same sentence 3 times


# solution 1

message = 'I have eaten ' + str(99) + ' burritos.'
print(message)

# solution 2:

number_of_burritor = 99
print(f'I have eaten {number_of_burritor} burritos')

#solution 3:

print('I have eaten ' + str(number_of_burritor) + 'burritos')


# Question 7: Why is eggs a valid variable name while 100 is invalid?
# Answer: Because variable names in python cannot start with a number.
# Question 8: What three functions can be used to get the integer, floating-point number, or string version of a value?
# Answer: int(), float(), str()