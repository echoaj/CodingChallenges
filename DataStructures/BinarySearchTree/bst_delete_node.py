
"""
    10
   / \
  1  20
 /  /  \
0  15   25
   /   /
  12  22
      /\
    21 24
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def show(node):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if node.right is None and node.left is None:
        line = '%s' % node.val
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.right is None:
        lines, n, p, x = show(node.left)
        s = '%s' % node.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.left is None:
        lines, n, p, x = show(node.right)
        s = '%s' % node.val
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = show(node.left)
    right, m, q, y = show(node.right)
    s = '%s' % node.val
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2

def display(root):
    tree = show(root)[0]
    for branch in tree:
        print(branch)
    print()

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def delete(node, val):
    # global tree
    if node is None:   # for when user enters value
        return node    # that does not exist in BST or root is none

    if val == node.val:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            left_tree = node.left
            right_tree = node.right
            cur = right_tree
            if cur.left is not None:
                while cur.left is not None:
                    parent = cur
                    cur = cur.left
                parent.left = delete(cur, cur.val)
                cur.right = right_tree
            cur.left = left_tree
            # if val == tree.val:
            #     tree = cur
            return cur

    if val < node.val:
        node.left = delete(node.left, val)
    else:
        node.right = delete(node.right, val)
    return node


tree = Node(10)
tree.left = Node(1)
tree.left.left = Node(0)
tree.right = Node(20)
tree.right.left = Node(15)
tree.right.left.left = Node(12)
tree.right.right = Node(25)
tree.right.right.left = Node(22)
tree.right.right.left.left = Node(21)
tree.right.right.left.right = Node(24)
display(tree)
print()
delete(tree, 10)
display(tree)