class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

nodeA = ListNode(7)
nodeB = ListNode(7)
nodeC = ListNode(7)
nodeD = ListNode(7)
#nodeE = ListNode(4)
#nodeF = ListNode(5)
#nodeG = ListNode(6)



nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = None
#nodeE.next = nodeF
#nodeF.next = nodeG
#nodeG.next = None



class Solution:
    def removeElements(self,head,val:int):
        current_node = head
        prev_node = None

        while current_node:
            if current_node.val == val:
                if prev_node:
                    prev_node.next = current_node.next
                else:
                    head = current_node.next
            else: 
            
                prev_node = current_node
            current_node = current_node.next
        return head
    
    def traversal(self,head):
        current_node = head

        while current_node:
            print(current_node.val)
            current_node = current_node.next


ans = Solution()
newHead = ans.removeElements(nodeA,7)
ans.traversal(newHead)