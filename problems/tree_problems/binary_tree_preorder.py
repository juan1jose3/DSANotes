
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []

        value = root.val

        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        return [value] + left + right
        


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

ans = Solution()

print(ans.preorderTraversal(root))