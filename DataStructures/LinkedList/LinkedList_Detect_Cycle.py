

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head.next.next

# o(n) space complexity
map = set()


# stop displaying once cycle or null is found
def display(ll_head):
    temp = ll_head
    while temp.next is not None:
        print(str(temp.data) + "-->", end=" ")
        temp = temp.next

        if temp not in map:
            map.add(temp)
        else:
            break

    print("\n Done")


display(head)


# o(1) space complexity
# cycle detector but with pointers
def detect_cycle(temp):
    move_by_1 = temp
    move_by_2 = temp

    while True:
        move_by_1 = move_by_1.next
        move_by_2 = move_by_2.next.next
        if move_by_1 is move_by_2:
            return True
        if move_by_2.next is None:
            return False


print(detect_cycle(head))
