# LeetCode
# 124. Binary Tree Maximum Path Sum
# Medium

"""
   -10
   / \
  9  20
    /  \
   15   7
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root):
    path_sum(root)
    return path


def path_sum(root):
    global path
    if root is None:
        return 0
    left_gain = max(0, path_sum(root.left))
    right_gain = max(0, path_sum(root.right))
    path = max(path, left_gain+right_gain+root.val) # calc max
    return max(left_gain, right_gain) + root.val


tree = Node(-3)
tree.left = Node(9)
tree.right = Node(20)
tree.right.left = Node(15)
tree.right.right = Node(7)

path = -110000
print(max_path_sum(tree))
