
''' Printing positive numbers in a list
'''


# Python program to print Positive Numbers in a List METHOD1

import numpy as np

list1 = np.array( [12, -7, 5, 64, -14])
print(list1)
pos_nos = list1[list1 >= 0];
print("Positive numbers in the list: ", pos_nos)

# Python program to print Positive Numbers in a List METHOD2

list1= [12, -7, 5, 64, -14]
print(list1)
for num in list1:
    if num>=0:
        print(f"The positive numbers are: {num}")
