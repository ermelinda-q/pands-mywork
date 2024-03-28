# Programming and Scripting - Week 7
# This file contains all code and answers in the quiz section of week 7
# Working with files

# 1.a
'''
with open("test-a.txt") as f:
    data = f.read()
    print(data)
# Q. what will happen if the file test-a.txt doesn't exist?
# A: if file doesn't exist the following code will give message:
# 'no such file or directory
'''
# 1.b.c 
'''
with open("test-b.txt", "w") as f:
    data = f.write("test b\n") # return the number of characters written
    print(data)    
with open("test-b.txt", "w") as f2: # open file again
    data = f2.write("another line\n")
    print(data)
# Q: What is the output of this program and what is the content of the file test-b.txt
# A: output is:
# 7
# 13
# Content of test-b.txt file is:
# another line
'''
# 1.d
# Q: what will the contents of this file be after this program is run.
# A: The program will create the file 'test-d.txt' will write the first line "test d" and a new line
# then will append the file with a second line "another line" and new line again
# it will display 7(number of characters) in the first line and 13(number of characters)in the second line.
'''
with open("test-d.txt", "w") as f:
    data = f.write("test d\n") # returns number of chars
    print(data)

with open("test-d.txt","a") as f2:
    data=f2.write("another line\n")
    print(data)
'''