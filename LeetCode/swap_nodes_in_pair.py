# Leetcode 24 Medium Problem: https://leetcode.com/problems/swap-nodes-in-pairs/

"""
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sawp_nodes_in_pair(head):
    if head is None or head.next is None:
        return head

    dummy = ListNode(0)
    dummy.next = head
    left, right, nxt = dummy, head, None
    while right and right.next:
        # right node's next node
        nxt = right.next
        # next node's next node - nxt_nxt
        nxt_nxt = right.next.next
        # set the leftv node's next to next node
        left.next = nxt
        right.next = nxt_nxt
        # set the leftv node's next to right node - swap
        nxt.next = right
        # set the right node's next to new next node
        # move to next state
        left = right
        right = right.next
    return dummy.next


def swap_nodes_in_pair_recursive(head):
    if head is None or head.next is None:
        return head

    temp = head.next
    head.next = swap_nodes_in_pair_recursive(head.next.next)
    temp.next = head
    return temp

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

node = sawp_nodes_in_pair(head)
while node:
    print(node.val)
    node = node.next
