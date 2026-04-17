# Graph Coloring using Backtracking

N = 7   # number of vertices
M = 3   # number of colors

# Adjacency Matrix
graph = [
    [0,1,1,1,0,0,0],
    [1,0,1,0,1,0,0],
    [1,1,0,1,0,1,0],
    [1,0,1,0,0,0,1],
    [0,1,0,0,0,1,1],
    [0,0,1,0,1,0,1],
    [0,0,0,1,1,1,0]
]

colors = [0] * N

# Check if safe
def is_safe(node, color):
    for i in range(N):
        if graph[node][i] == 1 and colors[i] == color:
            return False
    return True

# Backtracking function
def solve(node):
    if node == N:
        return True

    for c in range(1, M + 1):
        if is_safe(node, c):
            colors[node] = c

            if solve(node + 1):
                return True

            colors[node] = 0  # backtrack

    return False

# Main
if solve(0):
    print("Solution Found:\n")
    for i in range(N):
        print(f"Node {i} -> Color {colors[i]}")
else:
    print("No solution exists")