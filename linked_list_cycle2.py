class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None



head = ListNode(3)
nodeB = ListNode(2)
nodeC = ListNode(0)
nodeD = ListNode(-4)

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeB 


class Solution:

    def traversal(self,head):
        current_node = head
        while current_node:
            print(current_node.val)
            current_node = current_node.next


    def detectCycle(self,head):
        slow = head
        fast = head
        

        while fast and fast.next:
            

            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        
        return None


ans = Solution()
#ans.traversal(head)

print(ans.detectCycle(head))