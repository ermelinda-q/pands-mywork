# Programming and Scripting - Week 9
# Module of useful functions
# Based on week 9 lectures by Andrew Beatty
# Author: Ermelinda Qejvani

import logging 
logging.basicConfig(level=logging.DEBUG)
def fibonacci(number):
    a = 0
    b = 1
    fibonacci_sequence = [0]
    # we have one in the list already so number -1 times
    #this is not the most efficient code
    # could have used yield
    for i in range(1,number):
        fibonacci_sequence.append(b)
        # this code makes a=b and b=a+b
        a, b = b, a + b
    logging.debug("%d: %s", number, fibonacci_sequence)
    if number == 0:
        return []
    
    if number < 0:
        raise ValueError('number must be >0')

'''
return7 = [0,1,1,2,3,5,8]
return11 = [0,1,1,2,3,5,8,13,21,32,55]

try:
    fibonacci(-1)
except ValueError:
    # we want this exception to be thrown
    # so this is an example where we want to do nothing
    pass
else:
    # if the exception was not thrown we should throw
    # Assertion error
    assert False, 'fibonacci missing ValueError'
    # or
    # raise AssetionError("fibonacci no valueError!)
    # ")

assert fibonacci(7) == return7, 'incorrect return for 7'
assert fibonacci(11) == return11, 'incorrect return for 11'
assert fibonacci(0) == [], 'incorrect return value for 0'
assert fibonacci(1) == [0], 'incorrect return value for 1'

'''










if __name__ == '__main__':
    # tests will go here
    print("all good")