"""
Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7

Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
"""

# Might be better to put into a new tree.


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(t1, t2):
    if t1 is None:
        return t2

    if t2 is None:
        return t1

    t1.val += t2.val
    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)
    return t1


tree1 = Node(1)
tree1.left = Node(3)
tree1.left.left = Node(5)
tree1.right = Node(2)

tree2 = Node(2)
tree2.left = Node(1)
tree2.left.right = Node(4)
tree2.right = Node(3)
tree2.right.right = Node(7)

tree3 = mergeTrees(tree1, tree2)
print(tree3.val)
