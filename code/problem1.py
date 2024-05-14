# Let A be the set {1, 2, 3, 4}. Write a program to find the ordered pairs are in the relation
# I) R_1  = {(a, b) | a divides b}	II) R_2 = {(a, b) | a ≤ b}

# Variable initialization
from itertools import product

result_1 = []

# Getting Set Input From file
file_name = input("Enter file name with extension : ")  # code and input file should be in same folder

# read input value from file
file = open(file_name,"r")
Set = list(map(int, file.readlines()))

# Printing Set A
print("\n\nValue of the Set, A = ",Set,"\n")

# Calculating the ordered pairs
Data = list(product(Set,repeat=2))

# Calculating the ordered pair when relation following R1 ={(a,b) | a divides b}
for i,j in Data:
    if i%j==0 or j%i==0:
        result_1.append((i,j))

# Calculating the ordered pair when relation following R2 ={(a,b) | a ≤ b}
result_2 = [(i,j) for i,j in Data if i<=j]

# printing results
print ("The ordered pair list is for a / b : \n\t\t\t",result_1)
print ("The ordered pair list is for a <= b : \n\t\t\t" ,result_2)
file.close()
