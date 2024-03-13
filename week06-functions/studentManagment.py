# Programming and Scripting
# Week 6 - working with functions
# This program 
# 
# 
# 
# 
# Author: Ermelinda Qejvani



def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice
'''test the function
choice = displayMenu()
print(f"you chose {choice }")
'''
def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("enter name :")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit): ").strip()
    
    while moduleName != "":
        module = {}
        module["name"] = moduleName 
        # There is not error handling
        module["grade"] = int(input("\t\tEnter grade:"))
        modules.append(module)
        # read the next module name
        moduleName = input("\tEnter next module name (blank to quit):").strip()

    return modules
def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])
    
    print(students)
    

def displayModules(modules):
    print("\tName    \tGrade")
    for module in modules:
        print(f"\t{module['name']}   \t{module['grade']}")
        

# Main program
students = []
choice = displayMenu()
while(choice != 'q'):
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice != 'q':
        print("\n\nplease select either a,v or q")
    choice = displayMenu()

# adding students is in separate file named students.py


