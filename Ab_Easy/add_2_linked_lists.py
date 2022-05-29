# Leetcode problem: https://leetcode.com/problems/add-two-numbers/
# 2. Add Two Numbers Medium

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:
"""
    3582 + 967 = 4549
            1   1
    2-->8-->5-->3
    7-->6-->9   0  +
    -----------------
    9-->4-->5-->4
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_nums(l1, l2):
    sum_ll = ListNode(0)
    start = sum_ll
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val     # 2
            l1 = l1.next
        if l2:
            carry += l2.val     # 7
            l2 = l2.next
        num = carry % 10            # 9 % 10 = 9
        carry = carry // 10         # 9 // 10 = 0
        sum_ll.next = ListNode(num)
        sum_ll = sum_ll.next
    return start.next


head = ListNode(2)
head.next = ListNode(8)
head.next.next = ListNode(5)
head.next.next.next = ListNode(3)

head2 = ListNode(7)
head2.next = ListNode(6)
head2.next.next = ListNode(9)

node = add_two_nums(head, head2)

while node:
    print(node.val)
    node = node.next














'''
def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # Initialize a dummy node
    dummy = ListNode(0)
    # Initialize a pointer to the dummy node
    ptr = dummy
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        ptr.next = ListNode(carry % 10)
        ptr = ptr.next
        carry //= 10
    return dummy.next

'''