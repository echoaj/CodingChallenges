# LeetCode
# 113. Path Sum II
# Medium

"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


array = []
def pathSum(root, sum, path):
    if root is None:
        return

    path.append(root.val)
    if root.val == sum and root.left is None and root.right is None:    # reached leaf
        array.append(path)
        return

    pathSum(root.left, sum-root.val, path.copy())
    pathSum(root.right, sum-root.val, path.copy())



tree = Node(5)
tree.left = Node(4)
tree.left.left = Node(11)
tree.left.left.left = Node(7)
tree.left.left.right = Node(2)
tree.right = Node(8)
tree.right.left = Node(13)
tree.right.right = Node(4)
tree.right.right.left = Node(5)
tree.right.right.right = Node(1)

pathSum(tree, 22, [])
print(array)
