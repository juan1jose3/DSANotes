class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

nodeA = ListNode(1)
nodeB = ListNode(2)
nodeC = ListNode(3)
nodeD = ListNode(4)
nodeE = ListNode(5)
nodeF = ListNode(6)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF
nodeF.next = None


class Solution:
    def middleNode(self,head):
        fast = head
        slow = head
        

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
    

ans = Solution()
print(ans.middleNode(nodeA))