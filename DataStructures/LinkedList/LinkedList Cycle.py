# LeetCode
# 141. Linked List Cycle


def has_cycle(head):
    if head is None:
        return False
    tail = head.next

    while head != tail:
        if tail is None or tail.next is None:
            return False

        tail = tail.next.next
        head = head.next

    return True

# You could also used a hashmap to store
# nodes and check if duplicate node was found.
