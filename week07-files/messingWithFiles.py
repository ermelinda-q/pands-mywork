# Programming and Scripting
# Week 7 lab - Messing with files
# This program counts how many times it was run

# Author: Ermelinda Qejvani (Credits to Andrew Beatty)

# writing a function that reads in a number from a file that already exists

FILENAME = "count.txt"
def readNumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number
# test it
# num = readNumber()
# print(num)

# writing a function that takes in a number and overwrites a file with that number
# test it and check that the file has been changed

def writeNumber(number):
    with open(FILENAME, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))
#test it
# writeNumber(3)

# main
num = readNumber()
num +=1
print(f"we have run this program {num} times")
writeNumber(num)
