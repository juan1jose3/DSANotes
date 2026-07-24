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


class Solution:
    def inorderTraversal(self, root):
        left = []
        right = []
        
        if not root:
            return []

        if root.left:
           left = self.inorderTraversal(root.left)
           
        current = root.value
        
        
        

        if root.right:
            right = self.inorderTraversal(root.right)

        return left + [current] + right
        

        



root = Node(1)
root.right = Node(2)
root.right.left = Node(3)
sol = Solution()
print(sol.inorderTraversal(root))



    