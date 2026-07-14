class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value



def insert(node, value): 
    if not node:
        return Node(value)
    
    if value < node.value:
        node.left = insert(node.left, value)
    
    else:
        node.right = insert(node.right, value)
    return node

def inorder_traversal(node):
    if not node:
        return
    
    inorder_traversal(node.left)
    print(node.value)
    inorder_traversal(node.right)

def preorder_traversal(node):
    if not node:
        return
    
    print(node.value)

    preorder_traversal(node.left)
    preorder_traversal(node.right)


def find(node, value):

    if not node:
        return False 
    
    if value < node.value:
        return find(node.left ,value)
    
    elif value > node.value:
        return find(node.right ,value)
    else:
        return True


root = None

root = insert(root, 6)
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 1)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 19)
root = insert(root, 29)
root = insert(root, 11)
root = insert(root, 4)
root = insert(root, 2)

#preorder_traversal(root)
print(find(root,19))


