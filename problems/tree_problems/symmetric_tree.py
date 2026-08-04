class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root):
        ...

    def postOrderTraversal(self, root):
        if not root:
            return

        print(root.val)
        left = self.postOrderTraversal(root.left)
       
        right = self.postOrderTraversal(root.right)


node = TreeNode(1)
node.left = TreeNode(2)
node.left.left = TreeNode(3)
node.left.right = TreeNode(4)

node.right = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(3)

ans = Solution()
ans.postOrderTraversal(node)



