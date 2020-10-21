# LeetCode
# 102. Binary Tree Level Order Traversal
# Medium

"""
    3
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


def level_order(root):
    matrix = []
    level = [root]

    while root and level:
        visited = []
        next_level = []
        for node in level:
            visited.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level
        matrix.append(visited)

    return matrix


tree = Node(3)
tree.left = Node(9)
tree.right = Node(20)
tree.right.left = Node(15)
tree.right.right = Node(7)

print(level_order(tree))
