# Leetcode 86 Medium Problem: https://leetcode.com/problems/partition-list/

# Given a linked list and a value x,
# partition it such that all nodes less than x come before
# nodes greater than or equal to x.
# You should preserve the original relative order of the nodes

"""
Example: 1->4->3->2->5->2, x = 3
return 1->2->2->4->3->5
"""


class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition_list(head, x):
    if head is None or head.next is None:
        return head

    l_head = LinkedList()
    g_head = LinkedList()

    l_tail = l_head
    g_tail = g_head

    while head:
        if head.val < x:
            l_tail.next = LinkedList(head.val)
            l_tail = l_tail.next
        else:
            g_tail.next = LinkedList(head.val)
            g_tail = g_tail.next
        head = head.next

    l_tail.next = g_head.next
    return l_head.next


def display(node):
    while node:
        print(node.val)
        node = node.next


head = LinkedList(1)
head.next = LinkedList(4)
head.next.next = LinkedList(3)
head.next.next.next = LinkedList(2)
head.next.next.next.next = LinkedList(5)
head.next.next.next.next.next = LinkedList(2)
node = partition_list(head, 3)
display(node)
