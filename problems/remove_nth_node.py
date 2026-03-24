class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next


headA = ListNode(1)
nodeB = ListNode(2)
nodeC = ListNode(3)
nodeD = ListNode(4)
nodeE = ListNode(5)

headA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = None

class Solution:
    def traversal(self,head):
        current_node = head
        while current_node:
            print(current_node.val)
            current_node = current_node.next


    def removeNthFromEnd(self,head,n):
        dummy = ListNode(0)
        dummy.next = head
        current_head = dummy
        fast = dummy
        slow = dummy

        for _ in range(n+1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return current_head.next


ans = Solution()
new_head = ans.removeNthFromEnd(headA,2)
ans.traversal(new_head)