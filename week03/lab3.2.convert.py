# Programming and Scripting (coding with Python)

# Program Title: Converting floting numbers(positive * negative) to cents
# The program takes a number, converts it to its absolute value then 
# displays the value in cents.

# Author: Ermelinda Qejvani

# first we are assigning three variables:
# 1. input_value as a float number
# 2. input_abs_value as the absolute value of the input_value using abs() function
# 3. cent_value will be input_abs_value multiplyed by 100
# I thought to convert cent_value to integer because the value in cent
# displayed was xxx.0

input_value = float(input('Please enter an amount: '))
input_abs_value = abs(input_value)
cent_value = input_abs_value * 10 * 10  # multiplying by 100 gives sometime not the same result so I just multiplied the number twice by 10 

# The output will be : That amount in cent is and 'cent_value' will be displyed

print('That amount in cent is: {}'.format(cent_value))
