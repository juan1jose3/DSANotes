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
        

    
def max_depth(node):
    height = 0
    if not node:
        return 0

    height += 1
  
    left = max_depth(node.left) + height
    right = max_depth(node.right) + height

    return max(left, right)

    




root = None
root = insert(root, 50)
root = insert(root, 10)   # goes left
root = insert(root, 5)    # goes left-left
root = insert(root, 2)    # goes left-left-left
root = insert(root, 1)    # goes left-left-left-left
root = insert(root, 60)   # goes right (just one node on the right side)
print(max_depth(root))
