class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def averageOfLevels(self, root):
        avgs = []

        return self.get_avgs(root, avgs)

    def get_avgs(self, root, avgs):
        left = 0
        right = 0
        counter = 0
        
        if not root:
            return
       
        left = self.get_avgs(root.left, avgs)

       
        right = self.get_avgs(root.right, avgs)
            
        
            



root = TreeNode(3)
root.left = TreeNode(9)

root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)