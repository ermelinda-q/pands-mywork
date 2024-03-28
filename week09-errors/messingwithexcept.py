# Programming and Scripting - Week 9
# This program is to show how you can use try except
# Based on week 9 lectures by Andrew Beatty
# Author: Ermelinda Qejvani

# filename = data.txt
import sys 

# print (sys.argv)
try:
    filename = sys.argv[1]
    print(filename) 
    with open(filename) as fp:
        print(fp.read())
except IndexError as ie:
    print("Please enter the filename as an argument")
    # print(ie)
except FileNotFoundError:
    print(f"file {filename} not found, please enter a filename that exists")

