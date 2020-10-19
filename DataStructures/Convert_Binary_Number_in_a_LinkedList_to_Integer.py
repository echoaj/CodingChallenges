

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getDecimalValue(head):
    dec = 0
    while head is not None:
        dec = 2*dec + head.val
        head = head.next
    return dec


node = ListNode(1, ListNode(1, ListNode(0, ListNode(1))))
print(getDecimalValue(node))


# second way to convert binary to decimal

bin = "1101"
dec = 0

for bit in bin:
    dec *= 2
    dec += int(bit)

print(dec)

'''
0000 * 2    # shift left
0000 + 1    # add bit

0001 * 2    # shift left
0010 + 1    # add bit

0011 * 2    # shift left
0110 + 0    # add bit

0110 * 2    # shift left
1100 + 1    # add bit

1101        # 13


0 * 2       # x2
0 + 1       # add bit

1 * 2       # x2
2 + 1       # add bit

3 * 2       # x2
6 + 0       # add bit

6 * 2       # x2
12 + 1       # add bit

13          # Answer
'''