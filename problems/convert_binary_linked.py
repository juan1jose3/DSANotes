class ListNode:
    def __init__(self,val=0,next=0):
        self.val = val
        self.next = next


head = ListNode(1)
nodeB = ListNode(0)
nodeC = ListNode(1)

head.next = nodeB
nodeB.next = nodeC
nodeC.next = None

class Solution:
    def traversal(self,head):
        current_node = head
        while current_node:
            print(current_node.val)
            current_node = current_node.next


    def getDecimalValue(self,head):
        converted = 0
        current_node = head
        while current_node:
            
            converted *= 2
            converted += current_node.val
            current_node = current_node.next
        return converted

ans = Solution()

print(ans.getDecimalValue(head))