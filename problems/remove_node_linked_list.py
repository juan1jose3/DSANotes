class ListNode:
    def __init__(self,val=0, next=None) -> None:
        self.val = val
        self.next = next


head = ListNode(5)
nodeB = ListNode(2)
nodeC = ListNode(13)
nodeD = ListNode(3)
nodeE = ListNode(8)


head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = None



class Solution:
    def removeNodes(self, head):
        fast = head 
        slow = head
        prev = head 

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        
        


    def traversal(self, head):
        current_node = head
        while current_node:
            print(current_node.val)
            current_node = current_node.next
    

ans = Solution()
print(ans.removeNodes(head))
#ans.traversal(head)