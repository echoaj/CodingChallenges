
# most recently viewed things go to front of cache

class Node:
    def __init__(self, val=None, key=None):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


class LRU:
    def __init__(self, capacity):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
        self.size = capacity

    def get(self, key):
        if key not in self.map:
            return -1
        else:
            node = self.map[key]            # get node from map
            self.remove(node)               # remove from back of linked list
            self.add(node)                  # add it to front of linked list
            return node.val                 # return value of node


    def put(self, key, value):
        if key in self.map:                 # if we are overriding a node
            node = self.map[key]            # get node from map
            self.remove(node)               # remove from back of linked list
            node.val = value                # update value
            self.add(node)                  # add it to front of linked list
        else:
            if len(self.map) == self.size:  # check if reached capacity reached
                self.map.pop(self.tail.prev.key)    # if so remove from dict
                self.remove(self.tail.prev)         # if so remove from LL

            new_node = Node(key, value)     # Create new node
            self.add(new_node)
            self.map[key] = new_node


    # Puts node at front
    def add(self, node):
        head_next = self.head.next          #                  [hn] -> head.next
        node.next = head_next               #         node  -> [hn]
        head_next.prev = node               #         node  <- [hn]
        self.head.next = node               # [h]  -> node
        node.prev = self.head               # [h]  <- node


    # Remove node from back
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node


lru = LRU(3)
lru.put(5,5)
lru.put(8,8)
lru.put(2,2)
lru.put(7,7)
print(lru.get(4))
print(lru.get(5))
print(lru.get(2))