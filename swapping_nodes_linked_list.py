class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


head = ListNode(1)
nodeB = ListNode(2)
nodeC = ListNode(3)
nodeD = ListNode(4)
nodeE = ListNode(5)

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = None




class Solution:
    def swapNodes(self,head, k):
        current_head = head
        index = 1
        
        fast = head
        slow = head

        first = head

        for _ in range(k):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        
        while first:
            if index == k:
                break
            index+=1
            first = first.next

        temp = slow.val
        slow.val = first.val
        first.val = temp

        return current_head


    def traversal(self,head):
        current_node = head

        while current_node:
            print(current_node.val)
            current_node = current_node.next


ans = Solution()
print(ans.swapNodes(head,2))
ans.traversal(head)