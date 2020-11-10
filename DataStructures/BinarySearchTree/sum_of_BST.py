'''
LeetCode
129. Sum Root to Leaf Numbers
Medium


Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1

Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
'''


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root):
    if root is None:
        return 1

    if root.left is None and root.right is None:
        return root.val

    left = sumNumbers(root.left) * 1
    right = sumNumbers(root.right) * 1

    return left + right + root.val



tree = Node(4)
tree.left = Node(9)
tree.left.left = Node(5)
tree.left.right = Node(1)
tree.right = Node(0)
print(sumNumbers(tree))
