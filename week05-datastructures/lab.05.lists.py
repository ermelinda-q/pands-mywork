# This program gets 10 random numbers and creates a list. 
# Then the program takes the numbers from the queue one at a time
# prints the number and also prints the numbers left in the list
# the command pop[0] takes the first element out of a list.

# Programming and scripting

# Author: Ermelinda Qejvani

import random   # import random library
queue = []      # create list named queue where all numbers will be stored
number_of_numbers = 10   # setting how many numbers will the variable number_of_numbers store(10)
rangeTo = 100   # maximum number to created the list 100

for n in range(0, number_of_numbers) :   # 'for' loop n(variable) in the range 0-100
    queue.append(random.randint(0, rangeTo))   # append the list 'queue' adding an int randomly from 0-100

print(f"Queue is {queue}")    # print/display the list stored in 'queue'

while len(queue) != 0:      # using 'while' loop to keep running until there are no elements in the 'queue' list
    
    current_number = queue.pop(0)  # variable current_number will hold the first number[0]
                                    # and .pop() function removes the first number from the list
    # print first number in the list 'current_number', the message and what remains kin the list 'queue' after first element is removed.
    print(f"current Number is {current_number} and the queue is {queue}")
# when list 'queue' is empty display the following message:    
print ("The queue is no empty")


