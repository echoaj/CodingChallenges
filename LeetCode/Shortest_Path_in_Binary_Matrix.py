"""
LeetCode
1091 Shortest Path in Binary Matrix
Medium
"""

# Needs Work
def shortestPathBinaryMatrix(grid):
    queue = [[0,0]]
    h = len(grid)
    w = len(grid[0])
    end = [h-1, w-1]

    while queue:
        cord = queue.pop()
        print(cord)
        x = cord[0]
        y = cord[1]
        if x+1 < h and grid[x+1][y] == 0 and [x+1, y] not in queue:
            queue.append([x+1, y])
        if y+1 < w and grid[x][y+1] == 0 and [x, y+1] not in queue:
            queue.append([x, y+1])
        if x+1 < h and y+1 < w and grid[x+1][y+1] == 0 and [x+1, y+1] not in queue:
            queue.append([x+1, y+1])




def shortestPathBinaryMatrix(grid, i=0, j=0):
    if grid[i][j] == 1:
        return -1

    high = 1000

    if i+1 < h and j+1 < w:
        if grid[i+1][j] == 0:
            d = shortestPathBinaryMatrix(grid, i + 1, j) + 1
            high = min(d, high)
        if grid[i][j+1] == 0:
            r = shortestPathBinaryMatrix(grid, i, j + 1) + 1
            high = min(r, high)
        if grid[i+1][j+1] == 0:
            v = shortestPathBinaryMatrix(grid, i + 1, j + 1) + 1
            high = min(v, high)
        return high
    if j+1 < w:
        if grid[i][j+1]:
            r = shortestPathBinaryMatrix(grid, i, j+1) + grid[i][j] + 1
            high = min(r, high)
        return high
    if i+1 < h:
        if grid[i+1][j]:
            v = shortestPathBinaryMatrix(grid, i+1, j) + grid[i][j] + 1
            high = min(v, high)
        return high

    return 1


matrix = [[0,0,0],
          [1,1,0],
          [1,1,0]]

# matrix = [[0, 1, 1, 0, 1, 1, 0],
#           [0, 1, 1, 0, 0, 0, 1],
#           [0, 1, 0, 1, 1, 1, 0],
#           [0, 1, 0, 1, 1, 1, 0],
#           [0, 1, 1, 0, 1, 1, 0],
#           [0, 1, 1, 1, 0, 1, 0],
#           [1, 0, 0, 0, 1, 1, 0]]
#
# matrix = [[0,1,0],
#           [1,1,0],
#           [1,1,0]]

h = len(matrix)
w = len(matrix[0])
print(shortestPathBinaryMatrix(matrix))


