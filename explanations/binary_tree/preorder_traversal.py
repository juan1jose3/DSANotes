class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def preorder_traversal(self, node):
        left = []
        right = []
        if not node:
            return []

        value = node.value
        if node.left:
            left = self.preorder_traversal(node.left)
            
        
        if node.right:
            right = self.preorder_traversal(node.right)

        return [value] + left + right

        
            


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

ans = Solution()
print(ans.preorder_traversal(root))