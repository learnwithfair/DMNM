# The following table gives the population of a town during the last six censuses. Write a Python program to find the population in the year of 1946 using Newton-Gregory forward interpolation formula…………………………………………………... 19 - 23
# Year:	1911	1921	1931	1941	1951	1961
# Population:	12	15	20	27	39	52




from math import factorial

# calculating u
def u_cal(u, n):
    temp = u;
    for i in range(1, n):
        temp = temp * (u - i);
    return temp;

# read input value from file
file_name = input("Enter file name with extension: ")  # code and input file should be in same folder
file = open(file_name, "r")
data = file.read()
print("Values of table :")
print(data)
print()
data = data.split()
n = int(len(data)/2)
x,r = [],[]
for i, j in zip(data[0::2], data[1::2]):
    x.append(int(i))
    r.append(int(j))

# y[][] is used for difference table
y = [[0 for i in range(n)]
     for j in range(n)];

# with y[][0] used for input
for i in range(n):
    y[i][0] = r[i]

# Value to interpolate at
value = float(input("Enter value of x for interpolation: "));
print("\nForward difference table: ")
print("Here, x = Year and f(x) = Population")

# Calculating the forward difference table
for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

# Displaying the forward difference table
formated_table = ["x", "f(x)", "∇f(x)"]
for i in range(2, n+1):
    formated_table.append("∇^" + str(i) + "f(x)")
print("  ", end="")
for i in range(n+1):
    print(formated_table[i], end=" \t");
print()

for i in range(n):
    print(x[i], end="  \t");
    for j in range(n - i):
        if j>1:
            print(end="\t")
        print(y[i][j], end="\t\t");
    print();

# initializing u and sum
sum = y[0][0];
u = (value - x[0]) / (x[1] - x[0]);

# Result Calculation
for i in range(1, n):
    sum = sum + (u_cal(u, i) * y[0][i]) / factorial(i);

# Printing Result
print("\nValue at", value,
      "is", round(sum, 6));
