"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
"""



class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def same_tree(p, q):
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val != q.val:
        return False

    return same_tree(p.left, q.left) and same_tree(p.right, q.right)


tree = Node(3)
tree.left = Node(9)
tree.right = Node(20)
tree.right.left = Node(15)
tree.right.right = Node(7)

tree2 = Node(3)
tree2.left = Node(9)
tree2.right = Node(20)
tree2.right.left = Node(15)
tree2.right.right = Node(7)

print(same_tree(tree, tree2))