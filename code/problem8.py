# Write a Python program to find the value of f(15) from the following table using Newton’s divided difference formula for unequal intervals …………………… 28 - 32
# x:	4	5	7	10	11	13
# f(x):	48	100	294	900	1210	2028
#


# function defined
def u_cal(i, value, x):
    pro = 1
    for j in range(i):
        pro = pro * (value - x[j])
    return pro

# read input value from file
file_name = input("Enter file name with extension: ")  # code and input file should be in same folder
file = open(file_name, "r")
data = file.read()
print("Values of table :")
print(data,end="\n")
data = data.split()
n = int(len(data)/2)
x,r = [],[]
for i, j in zip(data[0::2], data[1::2]):
    x.append(int(i))
    r.append(int(j))

# y[][] is used for divided difference table
y = [[0 for i in range(n)]
     for j in range(n)];

# with y[][0] used for input
for i in range(n):
    y[i][0] = r[i]

# Value to interpolate at
value = float(input("Enter value of x for interpolation: "));
print()
# calculating divided difference table
for i in range(1, n):
    for j in range(n - i):
        y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) / (x[j] - x[i + j]))

# displaying divided difference table
print("Divided difference table:")
formated_table = ["x", "f(x)", "∇f(x)"]
for i in range(2, n+1):
    formated_table.append("∇^" + str(i) + "f(x)")
for i in range(n+1):
    print(formated_table[i], end="\t\t");
print()

for i in range(n):
    print(x[i], end="\t\t ");
    for j in range(n - i):
        print(y[i][j], end=" \t\t");
    print();

# initializing sum
sum = y[0][0];

# applying Newton's divided difference formula
# Result Calculation
for i in range(1, n):
    sum = sum + (u_cal(i,value,x) * y[0][i]);

# Printing Result
print("\nValue at", value,
      "is", round(sum, 2));
