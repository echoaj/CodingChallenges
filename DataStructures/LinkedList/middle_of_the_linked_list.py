# Leetcode 876 Easy Problem: https://leetcode.com/problems/middle-of-the-linked-list/

# Given a non-empty, singly linked list with head node head,
# return a middle node of linked list. If there are two middle nodes,
# return the second middle node.

"""
Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])

Example 2:
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_of_the_linked_list(head):
    if head is None or head.next is None:
        return head

    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
node = middle_of_the_linked_list(head)
while node:
    print(node.val)
    node = node.next
