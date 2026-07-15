class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(node,value):
    if not node:
        return Node(value)

    if node.value < value:
        node.left = insert(node.left, value)

    else:
        node.right = insert(node.right, value)

    return node



def sum_values(node):
    sum = 0
    if not node:
        return 0

    sum += node.value

    return sum_values(node.left) + sum_values(node.right) + sum
    



node = None
node = insert(node,6)
node = insert(node,5)
node = insert(node,2)

node = insert(node, 19)
node = insert(node, 29)

print(sum_values(node))