# LeetCode
# 226. Invert Binary Tree
# Easy

"""
Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

# don't understand too much


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def display(root):
    if not root:
        return
    print(root.val)
    display(root.left)
    display(root.right)


def invert_tree(root):
    if not root:
        return None
    n = invert_tree(root.left)
    d = invert_tree(root.right)
    root.right = n
    root.left = d
    return root


tree = Node(4)
tree.left = Node(2)
tree.left.left = Node(1)
tree.left.right = Node(3)
tree.right = Node(7)
tree.right.left = Node(6)
tree.right.right = Node(9)
invert_tree(tree)

display(tree)
