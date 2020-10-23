
"""
Given two non-empty binary trees s and t, check whether tree t has
exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2

Given tree t:
   4
  / \
 1   2

Return true, because t has the same structure and node values with a subtree of s.
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_subtree(s, t):
    return True


tree1 = Node(3)
tree1.left = Node(4)
tree1.left.left = Node(1)
tree1.left.right = Node(2)
tree1.right = Node(5)

tree2 = Node(4)
tree2.left = Node(1)
tree2.right = Node(2)

print(is_subtree(tree1, tree2))