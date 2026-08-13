from turtle import left


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def isBalanced(self, root):
        if not root:
            return True

        left_height = self.check_height(root.left)
        right_height = self.check_height(root.right)



        return abs(left_height - right_height) <= 1

      
        
    def check_height(self, root):
    
        left = 0
        right = 0

        if not root:
            return 0

    

        left = self.check_height(root.left) + 1
        right = self.check_height(root.right) + 1

        return max(left, right)
        

        


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)


ans = Solution()

print(ans.isBalanced(root))









