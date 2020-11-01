# Leetcode
# 21. Merge Two Sorted Lists
# Easy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    head = ListNode()
    temp = head
    while True:
        new_node = ListNode()
        if l1 is not None and l2 is not None:
            if l1.val < l2.val:
                new_node.val = l1.val
                l1 = l1.next
            else:
                new_node.val = l2.val
                l2 = l2.next
        elif l1 is not None:
            new_node.val = l1.val
            l1 = l1.next
        elif l2 is not None:
            new_node.val = l2.val
            l2 = l2.next
        else:
            break
        temp.next = new_node
        temp = temp.next

    return head.next


l1 = ListNode(1, ListNode(2, ListNode(4, ListNode(5))))
l2 = ListNode(1, ListNode(3, ListNode(4)))
node = mergeTwoLists(l1, l2)

print(node.val)