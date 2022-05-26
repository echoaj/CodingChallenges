
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(map, node):
    if node.val in map:
        return map[node.val]

    copy = Node(node.val)
    map[node.val] = copy                               # 1 -> Node(1)
    for adj in node.neighbors:                      # two adj nodes for 1  (2 & 3)
        copy.neighbors.append(cloneGraph(map, adj)) # place 2 and 3 as copy's neighboors
    return copy


graph = Node(1, [Node(2, [Node(4), Node(5)]), Node(3, [Node(7), Node(4)])])
print(graph.neighbors[0].neighbors[1].val)

new = cloneGraph({}, graph)