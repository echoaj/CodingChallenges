# Leetcode
# Symmetric Tree 101

"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root):
    if root is None:
        return True
    return sym(root.left, root.right)


def sym(left_node, right_node):
    if left_node is None is right_node:
        return True
    if left_node is None or right_node is None or left_node.val != right_node.val:
        return False

    return sym(left_node.left, right_node.right) and sym(left_node.right, right_node.left)


tree = Node(1)
tree.left = Node(2)
tree.left.left = Node(3)
tree.left.right = Node(4)
tree.right = Node(2)
tree.right.right = Node(3)
tree.right.left = Node(4)


print(isSymmetric(tree))