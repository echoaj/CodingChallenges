
"""
     9
   /  \
  7   15
 /   /  \
3  11   20
"""


class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def bfs(root):
    queue = [root]
    visited = []
    visited.append(root.data)
    while queue:
        top = queue.pop(0)
        if top.left:
            queue.append(top.left)
            visited.append(top.left.data)
        if top.right:
            queue.append(top.right)
            visited.append(top.right.data)
    print(visited)


tree = Node(9)
tree.left = Node(7)
tree.right = Node(15)
tree.left.left = Node(3)
tree.right.left = Node(11)
tree.right.right = Node(20)
bfs(tree)


def bfs(graph, start):
    queue = [start]
    visited = []
    visited.append(start)
    while queue:
        top = queue.pop(0)
        for adj in graph[top]:
            visited.append(adj)
            queue.append(adj)
    print(visited)


d = {9: [7, 15],
     7: [3],
     15: [11, 20],
     3: [],
     11: [],
     20: []}

bfs(d, 9)

