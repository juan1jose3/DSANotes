class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val = val
        self.next = next


head = ListNode(4)
nodeB = ListNode(2)
nodeC = ListNode(1)
nodeD = ListNode(3)

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = None

class Solution:
    def traversal(self,head):
        current_node = head
        while current_node:
            print(current_node.val)
            current_node = current_node.next

    def sortList(self,head):
        current_node = head
        values = []
        head_node = head

        while current_node:
            values.append(current_node.val)
            current_node = current_node.next
        values.sort()
    
        current_node = head
        index = 0
        while current_node:
            current_node.val = values[index]
            current_node = current_node.next
            index += 1
        return head_node
        



ans = Solution()
print(ans.sortList(head))
ans.traversal(head)