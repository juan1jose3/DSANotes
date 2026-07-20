class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def insert(node, value):
    if not node:
        return Node(value)

    if node.value < value:
        node.left = insert(node.left, value)

    else:
        node.right = insert(node.right, value)

    return node


def find_smallest(node):
    if not node:
        return float('inf')

    if not node.left and not node.right:
        return node.value

    return min(find_smallest(node.left), find_smallest(node.right) , node.value)

root = None
root = insert(root, 6)
root = insert(root, 5)
root = insert(root, 19)
root = insert(root, 2)
root = insert(root, 29)
print(find_smallest(root))