# LeetCode
# 104. Maximum Depth of Binary Tree
# Easy

"""
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    if not root:
        return 0
    return max(max_depth(root.left)+1, max_depth(root.right)+1)


tree = Node(3)
tree.left = Node(9)
tree.right = Node(20)
tree.right.left = Node(15)
tree.right.right = Node(7)
print(max_depth(tree))
