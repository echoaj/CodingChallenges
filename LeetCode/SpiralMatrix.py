# LeetCode Medium
# Spiral Matrix 54
# Needs Work


def printmat(matrix):
    print()
    for m in matrix:
        print(m)


def rotate(matrix):
    new = []
    for j in range(len(matrix[0])-1, -1 , -1):
        inner = []
        for i in range(len(matrix)):
            inner.append(matrix[i][j])
        new.append(inner)
    return new


def spiralOrder(matrix):

    for i in range(6):
        for i in matrix[0]:
            print(i, end=" ")
        matrix.pop(0)
        matrix = rotate(matrix)
    for i in matrix[0]:
        print(i, end=" ")

    # return matrix


mat = [[1, 2, 3, 4, 5],
       [1, 2, 3, 4, 5],
       [1, 2, 3, 4, 5],
       [1, 2, 3, 4, 5]]
spiralOrder(mat)
