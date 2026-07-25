class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def find_even(node):
    value = []
    left = []
    right = []
    if not node:
        return []

    if node.value % 2 == 0:
        value = [node.value]

    if node.left:
        left = find_even(node.left)

    if node.right:
        right = find_even(node.right)

    return value + left + right
        


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
print(find_even(root))