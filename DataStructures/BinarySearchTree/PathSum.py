
"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def hasPathSum(root, sum):
    if root is None:
        return False

    if root.val == sum and root.left is None and root.right is None:    # reached leaf
        print(root.val)
        return True

    found1 = hasPathSum(root.left, sum-root.val)
    found2 = hasPathSum(root.right, sum-root.val)
    return found1 or found2


tree = Node(5)
tree.left = Node(4)
tree.left.left = Node(11)
tree.left.left.left = Node(7)
tree.left.left.right = Node(2)
tree.right = Node(8)
tree.right.left = Node(13)
tree.right.right = Node(4)
tree.right.right.right = Node(1)

print(hasPathSum(tree, 22))

