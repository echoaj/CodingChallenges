# 2D list of 25 integers
graph = [[1, 2, 0, 4, 5],
         [6, 7, 8, 0, 10],
         [11, 12, 13, 0, 15],
         [16, 0, 18, 19, 20],
         [0, 22, 0, 24, 25]]

# visited = []


def dfs(x, y, visited):
    # base caseses
    # check if neighboor is out of bounds
    if x < 0 or x > len(graph[0]) - 1 or y < 0 or y > len(graph) - 1:
        return visited
    # check if the neighboor is in visited
    if (x, y) in visited or graph[x][y] == 0:
        return visited

    visited.append((x, y))
    for neighboor in [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]:
        dfs(*neighboor, visited)
    return visited


visited = dfs(0, 0, [])
for r, c in visited:
    print((r, c), graph[r][c])
