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

def find_max(node):

    if not node:
        return float('-inf')
        
    if node.left is None and  node.right is None:
        return node.value

    return max(find_max(node.left), find_max(node.right), node.value)

    

root = None
root = insert(root, 100)
root = insert(root, 1)
root = insert(root, 2)
print(find_max(root))
