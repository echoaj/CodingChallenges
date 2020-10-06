
class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None
        self.prev = None # NEW


class LRU:
    def __init__(self, k, v):
        self.dictionary = {k:v}
        self.capacity = 2
        self.head = Node(k, v)
        self.tail = self.head # NEW
        self.length = 1

    def full(self):
        if self.length > self.capacity:
            return True
        else:
            return False

    def put(self, key, value):
        self.append(key, value)
        self.dictionary[key] = value

        if self.full():
            key = self.head.key
            del self.dictionary[key]
            self.delete_front()
        print(self.dictionary)

    def get(self, key):
        try:
            result = self.dictionary[key]

            return result
        except KeyError:
            return -1

    def append(self, k, v):
        new_node = Node(k, v) # NEW
        new_node.prev = self.tail # NEW
        self.tail.next = new_node # NEW
        self.tail = self.tail.next # NEW
        self.length += 1

    def delete_front(self):
        temp = self.head
        self.head = self.head.next
        del temp
        self.head.prev = None # NEW
        self.length -= 1

    def print_backwards(self): #NEW
        cur = self.tail #NEW
        print(cur.key, cur.value) #NEW
        while cur.prev is not None: #NEW
            cur = cur.prev #NEW
            print(cur.key, cur.value) #NEW

    def size(self):
        return self.length


cache = LRU(1, 1)

cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))







'''
    def insert_front(self, k, v):
        new_node = Node(k, v)
        new_node.next = self.head
        self.head.prev = new_node # NEW
        self.head = new_node
        self.length += 1

    def insert_middle(self, pos, d):
        if pos <= 0:
            self.insert_front(d)
        elif pos >= self.length:
            self.append(d)
        else:
            cur = self.head
            for i in range(pos - 1):
                cur = cur.next
            temp = cur.next
            new_node = Node(d) # NEW
            cur.next = new_node # NEW
            new_node.prev = cur # NEW
            new_node.next = temp # NEW
            temp.prev = new_node # NEW
            self.length += 1
            
        def delete_back(self):
        temp = self.tail # NEW
        self.tail = self.tail.prev # NEW
        del temp # NEW
        self.tail.next = None # NEW
        self.length -= 1 # NEW

    def delete_middle(self, pos):
        if pos <= 0:
            self.delete_front()
        elif pos >= self.length:
            self.delete_back()
        else:
            cur = self.head
            for i in range(pos - 1):
                cur = cur.next
            temp = cur.next
            cur.next = temp.next
            cur.next.prev = cur # NEW
            del temp
            self.length -= 1

    def search(self, d):
        # returns number of that item found
        count = 0
        cur = self.head
        if cur.data == d:
            count += 1
        while cur.next is not None:
            cur = cur.next
            if cur.data == d:
                count += 1
        return count
    
    def print_forwards(self):
        cur = self.head
        print(cur.data)
        while cur.next is not None:
            cur = cur.next
            print(cur.data)
            
    
    def middle_node(self):
        cur = self.head
        center = int((self.size() - 0.5) / 2)
        for i in range(center):
            cur = cur.next
        return cur.data

    def reverse(self):
        prev = None

        self.tail = self.head
        while self.head is not None:
            next_node = self.head.next
            self.head.prev = next_node # New
            self.head.next = prev
            prev = self.head
            self.head = next_node
        self.head = prev


'''