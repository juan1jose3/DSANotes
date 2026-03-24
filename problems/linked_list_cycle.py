class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

nodeA = ListNode(3)
nodeB = ListNode(2)
nodeC = ListNode(0)
nodeD = ListNode(-4)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeB



class Solution:
    def hasCycle(self,head) -> bool:
       
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
            
        return False

        
        

   

ans = Solution()
print(ans.hasCycle(nodeA))

