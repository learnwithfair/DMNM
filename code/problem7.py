# Write a Python program to find f(7.5) form the following table using Newton-Gregory backward interpolation formula……………………………………………...…. 24 - 28
# x:	1	2	3	4	5	6	7	8
# f(x):	1	8	27	64	125	216	343	512



from math import factorial

# read input value from file
file_name = input("Enter file name with extension: ")  # code and input file should be in same folder
file = open(file_name, "r")
data = file.read()
print("Values of table :")
print(data,end="\n")
data = data.split()
x, y = [], []
for i, j in zip(data[0::2], data[1::2]):
    x.append(int(i))
    y.append(int(j))

# Value to interpolate at
inp = float(input("Enter value of x for interpolation: "))
print("\nBackward difference table: ")

# Calculating the backward difference table
table = [y]
for l in range(len(y) - 1):
    yn = []
    for i, k in zip(y[1::1], y[0::1]):
        yn.append(i - k)
    table.append(yn)
    y = yn

# Displaying the backward  difference table
formated_table = ["x", "f(x)", "∇f(x)"]
for i in range(2, len(table)+1):
    formated_table.append("∇^" + str(i) + "f(x)")
for i in range(len(table)+1):
    print(formated_table[i], end=" \t");
print()
for i in range(len(table)):
    print(x[i], end="  \t");
    for j in range(len(table) - i):
        if j>1:
            print(end="\t")
        print(table[j][i], end="\t\t");
    print();

# calculation of r
r = (inp - x[-1]) / (x[1] - x[0])

# result calculation
r_component = 1
partial_result = 0
for i in range(1, len(table)):
    r_component = r_component * (r + i - 1)
    partial_result = partial_result + (table[i][-1] * r_component) / factorial(i)
final_result = table[0][-1] + partial_result

# Printing Result
print("\nValue of", "f(",inp,") is : ", final_result);
