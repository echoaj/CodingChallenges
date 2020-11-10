'''
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1

sum is 4+9+0+5+1 = 19
'''


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumTree(root):
    if root is None:
        return 1

    if root.left is None and root.right is None:
        return root.val

    left = sumTree(root.left) * 1
    right = sumTree(root.right) * 1

    return left + right + root.val



tree = Node(4)
tree.left = Node(9)
tree.left.left = Node(5)
tree.left.right = Node(1)
tree.right = Node(0)
print(sumTree(tree))

