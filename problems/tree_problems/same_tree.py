class Node:
    def __init__(self, val=0, left=None, right=None):
             self.val = val
             self.left = left
             self.right = right



class Solution:
    def isSameTree(self,p, q):

        if (not p and q) or (p and not q):
            return False
            
        if not p and not q:
            return True

        if p.val != q.val:
            return False
            
        


        return  self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        
        
        
      
        

    
root = Node(1)
root.left = Node(2)
root.right = Node(1)


root_b = Node(1)
root_b.left = Node(1)
root_b.right = Node(2)
ans = Solution()

print(ans.isSameTree(root, root_b))