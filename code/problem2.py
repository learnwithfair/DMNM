# Suppose that A = {1, 2, 3} and B = {1, 2}. Let R be the relation from A to B containing (a, b) if a ∈ A, b ∈ B, and a > b.
# Write a program to find the relation R and also represent this relation in matrix form
# if a1 = 1, a2 = 2, and a3 = 3, and b1 = 1 and b2 = 2

import numpy as np

# Getting Set Input From file
file_name1 = input("Enter First file name with extension : ")  # code and input file should be in same folder
file_name2 = input("Enter Second file name with extension : ")  # code and input file should be in same folder

# reads input value from file
file1 = open(file_name1,"r")
file2 = open(file_name2,"r")
list1 = list(map(int, file1.readlines()))
list2 = list(map(int, file2.readlines()))

# using list comprehension
output1 = [(a, b) for a in list1
           for b in list2 if a > b]
data = [1 if a > b else 0 for a in list1
        for b in list2]

# Calculating matrix form relation of R
newArray = np.array(data)
output2 = newArray.reshape(4, 4)
# Printing Result
print("\nRelation of R : ",output1)
print("\nRepresent relation of R in matrix form is : \n",output2)
# Closing files
file1.close()
file2.close()
