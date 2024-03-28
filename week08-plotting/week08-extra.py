# Programming and Scripting - Week 8 extra activity
# This program is based on the week 8 labs of the above course
# The program is written to help one of my students create a bar chart for his maths CBA1
#

import numpy as np 
import matplotlib.pyplot as plt 

# creating the array for all items needed to adopt a puppy
data = {'Bed': 26.91, 'Bowl': 5, 'Food': 24.57, 'Toy1': 3, 'Toy2': 13, 'Collar': 9.76, 'Pads': 3.99, 'Other': 34.21}
items = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(8,5))

plt.bar(items, values, color = 'blue', width=0.8)

plt.xlabel("Essential Items")
plt.ylabel("Price of Items")

plt.title("Essential Items to Purchase")
# using bar charts

plt.show()
