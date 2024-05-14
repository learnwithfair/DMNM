# Write a program for graph coloring by Welch- Powell’s algorithm

# Function Declaration
def color_nodes(graph):
    color_map = {}

    # Consider nodes in descending degree (Most neighbors .... Least neighbors)
    for node in sorted(graph, key=lambda x: len(graph[x]), reverse=True):
        neighbor_colors = set(color_map.get(neigh) for neigh in graph[node])
        color_map[node] = next(
            color for color in range(len(graph)) if color not in neighbor_colors
        )
    return color_map

# Adjacent list
graph = {'a':list('bcd'),'b': list('ac'),'c': list('abdef'),'d': list('ace'),'e': list('cdf'),'f': list('ce')}
# Printing result
print("The solution of graph coloring problem by \'Welch-Powell’s\' algorithm is : \n",12 *"\t",color_nodes(graph))
