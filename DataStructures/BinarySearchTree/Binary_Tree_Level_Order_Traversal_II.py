# Leetcode
# 107. Binary Tree Level Order Traversal II
# Easy

"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
 /  /  \
11 15   7
"""

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderBottom(root):
    if root is None:
        return []
    visited = []
    queue = [root]
    while queue:
        level = []
        size = len(queue)
        for i in range(size):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        visited.append(level)
    return visited[::-1]


tree = Node(3)
tree.left = Node(9)
tree.right = Node(20)
tree.right.left = Node(15)
tree.right.right = Node(7)
tree.left.left = Node(11)
print(levelOrderBottom(tree))