
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
#  Needs Work

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


same = False
def is_subtree(s, t):
    global same
    if s is None:
        return
    if s.val == t.val:
        same = same_tree(s, t)
        return same
    if same is False:
        is_subtree(s.left, t)
        is_subtree(s.right, t)
    if same:
        return True
    else:
        return False


def same_tree(s, t):
    if not s and not t:
        return True
    elif not s or not t or s.val != t.val:
        return False

    return same_tree(s.left, t.left) and same_tree(s.right, t.right)



tree1 = Node(3)
tree1.left = Node(4)
tree1.left.left = Node(1)
tree1.left.right = Node(2)
tree1.right = Node(5)

tree2 = Node(4)
tree2.left = Node(1)
tree2.right = Node(2)

print(is_subtree(tree1, tree2))

# Solution
"""
def isMatch(self, s, t):
    if not(s and t):
        return s is t
    return (s.val == t.val and 
            self.isMatch(s.left, t.left) and 
            self.isMatch(s.right, t.right))

def isSubtree(self, s, t):
    if self.isMatch(s, t): return True
    if not s: return False
    return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
"""
