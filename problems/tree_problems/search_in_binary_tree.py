class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    
    def searchBST(self, root, val):
        if not root:
            return None

        if val < root.val:
           return self.searchBST(root.left, val)
           
        elif val > root.val:
            return self.searchBST(root.right, val)
            
        else:
            return root

        
            


root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right = TreeNode(7)

ans = Solution()
print(ans.searchBST(root,2))