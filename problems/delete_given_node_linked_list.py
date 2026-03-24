class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

nodeA = ListNode(4)
nodeB = ListNode(5)
nodeC = ListNode(1)
nodeD = ListNode(9)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = None

class Solution:
    def traversal(self,node):
        current_node = node
        while current_node:
            print(current_node.val)
            current_node = current_node.next

    def deleteNode(self,node):
        node.val = node.next.val
        nextNode = node.next.next
        
        node.next = nextNode
         

ans = Solution()
ans.deleteNode(nodeB)
ans.traversal(nodeA)