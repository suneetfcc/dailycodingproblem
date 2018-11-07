"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node, delim=';'):
    queue = deque()
    results = []
    queue.append(node)

    while queue:
        n = queue.popleft()
        if not n:
            results.append('#')
        else:
            results.append(n.val)
            queue.append(n.left)
            queue.append(n.right)

    return delim.join(results)


def deserialize(nodestr, delim=';'):

    nodelist = nodestr.split(delim)
    nodes = []
    for i,n in enumerate(nodelist):
        if n != '#':
            node = Node(n)
            nodes.append(node)
            if i % 2 == 0:
                parent = (i - 2) // 2
                if parent >= 0:
                    nodes[parent].right = node
            else:
                parent = (i - 1) // 2
                if parent >= 0:
                    nodes[parent].left = node

    return nodes[0]
