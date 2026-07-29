class Node:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right



class Solution:
    def maxDepth(self, root):
        counter = 0
        left = 0
        right = 0
        if not root:
            return counter
        counter += 1

        left = self.maxDepth(root.left) + counter
        right = self.maxDepth(root.right) + counter

        return max(left, right)



root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

ans = Solution()
print(ans.maxDepth(root))