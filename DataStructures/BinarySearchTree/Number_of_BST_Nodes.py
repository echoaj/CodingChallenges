
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


def node_count(root):
    if not root:
        return 0
    return node_count(root.left) + node_count(root.right) + 1


def sum_of_leafs(root):
    if root.left is None and root.right is None:
        return root.val
    return sum_of_leafs(root.left) + sum_of_leafs(root.right)


def sum_of_all_nodes(root):
    if not root:
        return 0
    return root.val + sum_of_all_nodes(root.left) + sum_of_all_nodes(root.right)


tree = Node(3)
tree.left = Node(9)
tree.right = Node(20)
tree.right.left = Node(15)
tree.right.right = Node(7)


print("Number of Nodes:\t", node_count(tree))
print("Sum of Leaves:\t", sum_of_leafs(tree))
print("Sum of all Noes:\t", sum_of_all_nodes(tree))
