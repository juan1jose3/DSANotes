class ListNode:
    def __init__(self,val=0, next=None) -> None:
        self.val = val
        self.next = next

    


head = ListNode(1)
nodeA = ListNode(2)
nodeB = ListNode(3)
nodeC = ListNode(4)



head.next = nodeA
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = None


class Solution:
    def traversal(self, head):
        current_node = head


        while current_node:
            print(current_node.val)
            current_node = current_node.next


    def reorderList(self, head):
        current_list_head = head
    
        fast = head
        slow = head

        # we get the left middle
        while fast.next and fast.next.next: # like this
            fast = fast.next.next
            slow = slow.next
        
        

        second_half = slow.next
        slow.next = None

        next_node = None
        prev_node = None
        
        while second_half:
                next_node = second_half.next
                second_half.next = prev_node
                prev_node = second_half
                second_half = next_node
        
        pointerA = current_list_head
        pointerB = prev_node


        while pointerB:
            tempA = pointerA.next
            tempB = pointerB.next

            pointerA.next = pointerB
            pointerB.next = tempA

            pointerA = tempA
            pointerB = tempB
            
                 

        
        




ans = Solution()
print(ans.reorderList(head))
ans.traversal(head)
