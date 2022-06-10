# Leetcode 83 - Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Given the head of a sorted linked list, delete all duplicates such that
# each element appears only once. Return the linked list sorted as well.

# If the list is not guranteed to be sorted you can use a set
# Otherwise you can get away without using a set


"""
Example 1:
    1->1->2
    Output: 1->2

Example 2:
    1->1->2->3->3
    Output: 1->2->3
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def display(head):
    while head is not None:
        print(head.val)
        head = head.next


def deleteDuplicates(head):
    if head is None:
        return head

    cur = head
    prev = head
    cache = set()
    while cur:
        if cur.val in cache:
            prev.next = cur.next
        else:
            cache.add(cur.val)
            prev = cur
        cur = cur.next
    return head


# without set
def deleteDuplicates2(head):
    curr = head

    while curr:
        while curr.next and curr.val == curr.next.val:
            curr.next = curr.next.next
        curr = curr.next

    return head


head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
node = deleteDuplicates(head)
display(node)
print()
node = deleteDuplicates2(head)
display(node)
