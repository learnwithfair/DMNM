# Write a program to find shortest path by Warshall’s algorithm
INF = 1000000000
def floyd_warshall(vertex, adjacency_matrix):

  # calculating all pair shortest path
  for k in range(0, vertex):
    for i in range(0, vertex):
      for j in range(0, vertex):

        # relax the distance from i to j by allowing vertex k as intermediate vertex
        # consider which one is better, going through vertex k or the previous value
        adjacency_matrix[i][j] = min(adjacency_matrix[i][j], adjacency_matrix[i][k] + adjacency_matrix[k][j])

  # pretty print the graph
  # o/d means the leftmost row is the origin vertex
  # and the topmost column as destination vertex
  print("Shortest path by \'Warshall’s\' algorithm is : \n")
  print("\t\t\t\t\t\t\t\t\t\to/d", end='')
  for i in range(0, vertex):
    print("\t\t\t{:d}".format(i+1), end='\t ')
  print();
  for i in range(0, vertex):
    print("\t\t\t\t\t\t\t\t\t\t{:d}".format(i+1), end='')
    for j in range(0,vertex):
        if i==0:
            print(end=" \t")
        if j>=1 and i<=j:
            print(end="\t ")
        if i ==1 and j == 2 or i ==1 and j == 3 or i ==2 and j == 3:
            print(end=" \t")
        print("\t\t{:d}".format(adjacency_matrix[i][j]), end='')
    print();

"""
input is given as adjacency matrix,
input represents this undirected graph
 A--1--B
 |    /
 3   /
 |  1
 | /
 C--2--D
should set infinite value for each pair of vertex that has no edge
 """
adjacency_matrix = [
          [   0,   5,  INF,  10],
          [  INF,  0,   3,  INF],
          [  INF,  INF, 0,    1],
          [  INF,  INF, INF,  0]
          ]
# Calling function
floyd_warshall(4, adjacency_matrix);
