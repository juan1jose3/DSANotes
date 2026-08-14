class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []

        
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
            
        current_value = root.val

        return  left + right + [current_value]



root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

ans = Solution()
print(ans.postorderTraversal(root))