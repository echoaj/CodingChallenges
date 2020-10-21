# LeetCode
# 143. Reorder List
# Medium


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head):
    if head is None:
        return head

#   Find Middle Node
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

#   Split in two lists
    mid = slow
    slow = slow.next
    mid.next = None

#   Reverse
    prev = None
    while slow:
        curr = slow
        slow = slow.next
        curr.next = prev
        prev = curr

#   Merge
    cur1 = head # 1 2 3
    cur2 = prev # 5 4

    while cur1 and cur2:
        temp1 = cur1.next
        temp2 = cur2.next
        cur1.next = cur2
        cur1 = temp1
        cur2.next = cur1
        cur2 = temp2

    return head


l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
node = reorderList(l1)

# Display new list
while node is not None:
    print(node.val)
    node = node.next
