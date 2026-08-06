
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def isUnivalTree(self, root):
        seen = set()
        
        return self.compareValues(root ,seen)
       

    def compareValues(self, root, seen):
        if not root:
            return True

        if root.val not in seen:
            seen.add(root.val)

        self.compareValues(root.left, seen)
        self.compareValues(root.right, seen)

        return len(seen) == 1
            
        



root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)
root.right.right = TreeNode(1)


ans = Solution()

print(ans.isUnivalTree(root))

