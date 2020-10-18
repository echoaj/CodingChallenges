# LeetCode
# 234. Palindrome Linked List
# Easy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time O(n)
# Space O(2)
def is_palindrome(head):
    array = []
    while head is not None:
        array.append(head.val)
        head = head.next
    return array == array[::-1]


node = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(is_palindrome(node))



# Time O(n)
# Space O(1)
# def is_palindrome(head):
#     slow = head
#     fast = head
#     while fast is not None and fast.next is not None:
#         slow = reversed(slow)
#         fast = head
#
#         while(slow is not None):
#             if slow.val is not fast.val:
#                 return False
#             slow = slow.next
#             fast = fast.next
#     return True
#
# def reversed():
#     pass