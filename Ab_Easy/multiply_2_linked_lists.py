

'''
Multiply two linked lists together.

eg. [2]->[5]->[9] * [1]->[3]->[6]->[2]

Hint: you are not allowed to simply convert the LL to an int and multiply like normal.
'''

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


num1 = Node(2)
num1.next = Node(5)
num1.next.next = Node(9)

num2 = Node(1)
num2.next = Node(3)
num2.next.next = Node(6)
num2.next.next.next = Node(2)


# loop 1
# 2
# loop 2
# 2 * 10 + 5
# 25
# loop 3
# 25 * 10 + 9
# 259
# total1 = 259
# total2 = 1362


def get_int(head):
    total = head.data
    while head.next:
        head = head.next
        val = head.data
        total *= 10
        total += val
    return total


def multiply(num1, num2):
    return get_int(num1) * get_int(num2)


result = multiply(num1, num2)
print(result, result == 259 * 1362)