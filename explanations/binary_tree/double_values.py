class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None



def postorder_traversal(node):
    left = []
    right = []
    if not node:
        return[]

    if node.left:
        left = postorder_traversal(node.left)

    if node.right:
        right = postorder_traversal(node.right)

    value = node.value

    return left + right + [value, value] 
    



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
print(postorder_traversal(root))
    