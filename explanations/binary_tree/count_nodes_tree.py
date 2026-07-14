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

def count_nodes(node):
    counter = 0
    if not node:
        return 0
       
    counter += 1

    return (count_nodes(node.left) + count_nodes(node.right) + counter)
   
    
    
    

    

    



node = None
node = insert(node,6)
node = insert(node,5)
node = insert(node,2)

node = insert(node, 19)
node = insert(node, 29)

print(count_nodes(node))
