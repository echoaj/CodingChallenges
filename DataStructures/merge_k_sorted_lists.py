# LeetCode
# 23. Merge k Sorted Lists
# Hard


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    array = []
    # O(n*k)
    for head in lists:
        while head is not None:
            array.append(head.val)
            head = head.next

    # O(n*k log(n*k))
    array.sort()

    # O(n)
    new = ListNode()
    temp = new
    for i in array:
        temp.next = ListNode(i)
        temp = temp.next
    return new.next


l1 = ListNode(1, ListNode(2, ListNode(4, ListNode(5))))
l2 = ListNode(1, ListNode(3, ListNode(6)))
l3 = ListNode(4, ListNode(7, ListNode(8)))
node = mergeKLists([l1, l2, l3])
# Display new list
while node is not None:
    print(node.val)
    node = node.next