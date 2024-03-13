# Programming and Scripting 
# Week 5 extra lab
# This program reads a student's name, module names and grades until a blank module name is entered.
# Author: Ermelinda Qejvani
''''
student_names = []     # creating a list for student names

student_name = input("Please enter student name: ")
if student_name != str:
    print("Thank you for your entry.\nGoodbye")
else:
    student_names.append(student_name)
    print(f"Student name is: {student_names}")
 '''   

# code 2 

cancel = False
student_list = []

while (True):
    name = input("Enter student name: ")
    module = input("Enter module: ")
    result = int(input("Module result: "))

    student_list.append({
        "name": name,
        "module": module,
        "result": result
    })

    cont = input("Want to add another? (Y/N)")
    if cont != "Y":
        break;

print(student_list)
