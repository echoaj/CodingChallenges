# Leetcode 73 - Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeros/
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

"""
Example 1:
Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
"""

# Follow up:
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

# A better solution is to replace the all 0 elements with #
# and then replace all the # elements with 0s.

# There is a solution even better than the one above with O(1) space.
# The idea is to use the first row and first column as marker.
# If there is a 0 in the first row or first column, then we will mark that row and column with 0.
# Then we will mark all the other elements with 0.


def setZeroes(matrix, lst):
    for x, y in lst:
        for i in range(len(matrix)):
            matrix[i][y] = 0
        for i in range(len(matrix[0])):
            matrix[x][i] = 0


def set_matrix_zeros(matrix):
    lst = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                lst.append((i, j))
    setZeroes(matrix, lst)


mat = [
    [1, 2, 3, 4],
    [5, 6, 0, 8],
    [9, 10, 11, 12],
    [0, 14, 15, 16]]

set_matrix_zeros(mat)
for m in mat:
    print(m)