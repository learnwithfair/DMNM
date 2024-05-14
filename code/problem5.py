# Suppose that the relations R1 and R2 on a set A are represented by the matrices
# M_R1=[■(1&0&1@1&0&0@0&1&1)] and M_R2=[■(1&0&1@0&1&1@1&0&1)]. Write a program to find the MR1∪R2 and MR1∩R2
#


# First Function
def matrix_intersection(mat1, mat2):
    mat_inter = []
    for rows in range(len(mat1)):
        List = []
        print(4 * "\t", end=" ")
        for cols in range(len(mat1[0])):
            List.append(mat1[rows][cols] and mat2[rows][cols])
            print(mat1[rows][cols] and mat2[rows][cols], end=" ") # Calculating intersection
        mat_inter.append(List)
        print()

    return mat_inter

# second function
def matrix_union(mat1, mat2):
    mat_union = []
    for rows in range(len(mat1)):
        List = []
        print(4 * "\t", end=" ")
        for cols in range(len(mat1[0])):
            List.append(mat1[rows][cols] or mat2[rows][cols])
            print(mat1[rows][cols] or mat2[rows][cols], end=" ")  # Calculating union
        mat_union.append(List)
        print()

    return mat_union

# Input declared Matrix1 and Matrix2
matrix1 = [[1, 0, 1],
           [1, 0, 0],
           [0, 1, 1]]
matrix2 = [[1, 0, 1],
           [0, 1, 1],
           [1, 0, 1]]

# printing First Matrix
print('First Matrix M_R1: ')
for rows in range(len(matrix1)):
    print(4*"\t",end=" ")
    for cols in range(len(matrix1[0])):
        print(matrix1[rows][cols],end=" ")
    print()

# printing Second Matrix
print('Second Matrix M_R2: ')
for rows in range(len(matrix2)):
    print(4*"\t",end=" ")
    for cols in range(len(matrix2[0])):
        print(matrix2[rows][cols],end=" ")
    print()

# printing Rows and Columns of matrix
print("\nRows:",len(matrix1),"; Cols:",len(matrix1[0]))

# printing Matrix Intersection
print('\nMatrix Intersection:')
mi = matrix_intersection(matrix1, matrix2)

# printing Matrix Union
print('Matrix Union: ')
mu = matrix_union(matrix1, matrix2)

v = ['p', 'q', 'r']

r1 = []
for i in range(len(mi)):
    for j in range(len(mi[0])):
        if mi[i][j] == 1:
            r1.append((v[i], v[j]))

print(r1)

r2 = []
for i in range(len(mu)):
    for j in range(len(mu[0])):
        if mu[i][j] == 1:
            r2.append((v[i], v[j]))

print(r2)
