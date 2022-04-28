# Rules

# Cache has a capacity *
# Get a value using key, return if it exists otherwise return -1*
# Put Key, value into cache
# If Key exists, update value*
# Otherwise add key-value pair to cache
# If full remove least recently used key

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRU:
    def __init__(self, cap):
        self.capacity = cap
        self.map = {}       # keep track of nodes
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key):
        if key in self.map:
            # Update to more recently
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            # Get Value
            return self.map[key].value
        else:
            return -1

    def insert(self, node):
        last_node = self.right.prev
        node.prev = last_node
        last_node.next = node
        node.next = self.right
        self.right.prev = node

    @staticmethod
    def remove(node):
        node.prev.next, node.next.prev = node.next, node.prev

    def put(self, key, value):
        # Update
        if key in self.map:
            self.map[key].value = value
        else:
            # Insert
            node = Node(key, value)
            self.insert(node)
            self.map[key] = node
            # Check if Full
            if len(self.map) > self.capacity:
                lru_node = self.left.next
                self.remove(lru_node)
                del self.map[lru_node.key]


lru = LRU(3)
lru.put(5, 5)
lru.put(8, 8)
lru.put(2, 2)
lru.put(7, 7)
print(lru.get(4))
print(lru.get(5))
print(lru.get(2))

