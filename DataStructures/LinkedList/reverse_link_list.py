# LeetCode
# 206. Reverse Linked List
# Easy

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    prev = None
    next_node = head.next

    while next_node is not None:
        head.next = prev
        prev = head
        head = next_node
        next_node = next_node.next
    head.next = prev

    return head


# Better Solution
def reverseList(head):
    prev = None
    while head.next:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return head



l1 = ListNode(1, ListNode(2, ListNode(4, ListNode(5))))
node = reverseList(l1)
print(node.val)