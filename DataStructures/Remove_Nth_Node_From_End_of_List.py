# LeetCode
# Medium
# 19. Remove Nth Node From End of List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    dummy = ListNode()
    dummy.next = head

    slow = dummy
    fast = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next



l1 = ListNode(1, ListNode(2, ListNode(4, ListNode(5, ListNode(6)))))
node = removeNthFromEnd(l1, 2)
while node:
    print(node.val)
    node = node.next

# s f
# dum -> 1 -> 2 -> 4 -> 5 -> 6 -> None

# s                f
# dum -> 1 -> 2 -> 4 -> 5 -> 6 -> None

#                  s                f
# dum -> 1 -> 2 -> 4 -> 5 -> 6 -> None

#                  s           f
# dum -> 1 -> 2 -> 4 -> 5 -> None