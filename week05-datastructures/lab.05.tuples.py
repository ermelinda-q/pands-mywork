# This program creates a tuple(list) storing months of the year
# and another tuple(list) storing summer months. It prints out
# the summer months
# Based on week 5 labs - programming and scripting by Andrew Beatty
# Author: Ermelinda Qejvani

# variable months will store all months of the year
months = ("January", 
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"
)
summer = months[4:7]   # variable summer will store months 
                        # indexed 4(May) to 7(7th month - August is not included)
                        
for month in summer: # calling the 'for' loop to print month (a newly created variable) 
    print(month)    # that reads from summer values and prints them out one by one. 'for' loop - as long as the condition is satisfied.