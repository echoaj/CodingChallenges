# Leetcode
# 297 Serialize and Deserialize Binary Tree
# Hard


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# encrypted = ""
# def serialize(root):
#     global encrypted
#     if root is None:
#         return
#     encrypted += str(root.val) + " "
#     serialize(root.left)
#     serialize(root.right)
#
#
#
# def deserialize():
#     global encrypted
#     array = encrypted.split()
#     print(array)
#     bt = Node(int(array[0]))
#     for i in range(1, len(array)):
#         val = int(array[i])
#         cur = bt
#         while True:
#             if val <= cur.val:
#                 if cur.left is None:
#                     cur.left = Node(val)
#                     break
#                 else:
#                     cur = cur.left
#             else:
#                 if cur.right is None:
#                     cur.right = Node(val)
#                     break
#                 else:
#                     cur = cur.right
#     return bt

# Answer
def serialize(root):
    def doit(node):
        if node:
            vals.append(str(node.val))
            doit(node.left)
            doit(node.right)
        else:
            vals.append('#')

    vals = []
    doit(root)
    return ' '.join(vals)

def deserialize(data):
    def doit():
        val = next(vals)
        if val == '#':
            return None
        node = Node(int(val))
        node.left = doit()
        node.right = doit()
        return node

    vals = iter(data.split())
    return doit()


def printree(tree):
    if tree is None:
        return
    print(tree.val)
    printree(tree.left)
    printree(tree.right)


tree = Node(4)
tree.left = Node(2)
tree.left.left = Node(1)
tree.left.right = Node(3)
tree.right = Node(7)
tree.right.left = Node(6)
tree.right.right = Node(9)

printree(tree)
string = serialize(tree)
print(string)
new = deserialize(string)
printree(new)