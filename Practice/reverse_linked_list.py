

class LinkNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def display_linked_list(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print()


def reverse_linked_list(head):
    l = head
    r = head.next
    prev = None

    while r:
        l.next = prev
        prev = l
        l = r
        r = r.next
    l.next = prev
    return l


head = LinkNode(1)
head.next = LinkNode(2)
head.next.next = LinkNode(3)
head.next.next.next = LinkNode(4)
head.next.next.next.next = LinkNode(5)
node = reverse_linked_list(head)
display_linked_list(node)
