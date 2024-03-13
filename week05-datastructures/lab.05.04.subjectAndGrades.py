# This program stores a students name and a list of her courses
 # and grades in a dict. The program should then print out her data.
 
 # Module - Programming and Scripting
 
 # Author: Ermelinda Qejvani
 
 # creating a dictionary named 'student'.
 # the 'student' dictionary is storing data for:
 # 'name' - name of student, in this case 'Mary'
 # 'modules' - is a list storing information in the form of 2 dictionaries inside
 # 'course_name' and 'grade' are stored in the dictionaries
student = {
     "name": "Mary",
     "modules": [
         {
             "course_name":"Programming",
             "grade": 45
         },
         {
             "course_name":"History",
             "grade": 99
         }
     ]
 }
print("Student: {}".format(student["name"])) # print student name
for module in student ["modules"]:  # for loop, run through 'modules list, assign value to 'module' variable
     print("\t {} \t: {}".format(module["course_name"], module["grade"]))