# LeetCode
# 142. Linked List Cycle II
# Medium


# O(n) space
# O(n) Time
def detect_cycle(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None:
        return None

    hashtable = set()
    while head is not None:
        if head in hashtable:
            return head
        hashtable.add(head)
        head = head.next

    return None



# seconds way
# two pointer method
# O(n) time
# O(1) space
def has_cycle(head):
    if head is None:
        return False
    fast = head.next
    slow = head

    while fast is not None or fast is not None:
        if fast is None or fast.next is None:
            return False

        if slow is fast:
            while slow is not head:
                slow = slow.next
                head = head.next
            return slow

        fast = fast.next.next
        slow = slow.next

    return True