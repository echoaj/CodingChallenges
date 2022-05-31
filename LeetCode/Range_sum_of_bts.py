# Leetcode 938 Easy, use to be Medium
# Problem: https://leetcode.com/problems/range-sum-of-bst/

# Given the root node of a binary search tree, return the sum
# of values of all nodes with value between L and R (inclusive).

"""
Example 1:
           10
          /  \
         5    15
        /    / \
       3    7  18
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:
              10
             /  \
            5    15
           / \   / \
          3   7  13  18
         /   /
        1   6
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Bad Solution O(n)
def range_sum_bst(root, low, high):
    global total
    # if root.left.val < low:
    #     return total
    # if root.right.val > high:
    #     return total
    # inorder traversal
    if root:
        range_sum_bst(root.left, low, high)
        total += root.val if low <= root.val <= high else 0
        range_sum_bst(root.right, low, high)

# Best Solution uses bfs


total = 0
head = TreeNode(10)
head.left = TreeNode(5)
head.right = TreeNode(15)
head.left.left = TreeNode(3)
head.left.right = TreeNode(7)
head.right.left = TreeNode(13)
head.right.right = TreeNode(18)
head.left.left.left = TreeNode(1)
head.left.left.right = TreeNode(6)
print(range_sum_bst(head, 6, 10))
print(total)
