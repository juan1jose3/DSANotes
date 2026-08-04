class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:
    def sortedArrayToBST(self,nums):
        return self.buildTree(nums, 0, len(nums) - 1)


    def buildTree(self, nums ,start, end):

        if start > end:
            return 
            
        middle = start + (end - start) // 2

        root = TreeNode(nums[middle])

        root.left = self.buildTree(nums, start, middle - 1)
        root.right = self.buildTree(nums, middle + 1, end)

        return root
    
        

        
    

        
            
            

list = [-10, -3, 0, 5, 9]
ans = Solution()

root = ans.sortedArrayToBST(list)

print(root.val)
print(root.left.val)
print(root.left.right.val)

print("Right side")

print(root.right.val)
print(root.right.right.val)


    