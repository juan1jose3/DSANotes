class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


nodeA = ListNode(1)
nodeB = ListNode(1)
nodeC = ListNode(2)
nodeD = ListNode(3)
nodeE = ListNode(3)

nodeA.next = nodeB
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

    def deleteDuplicates(self,head):
        current_node = head
        new_head = head
        prev_node = None
        numbers = set()
        while current_node:
            if current_node.val in numbers:
                prev_node.next = current_node.next
            else:
                numbers.add(current_node.val)
                prev_node = current_node
            current_node = current_node.next
        return head


ans = Solution()
ans.deleteDuplicates(nodeA)
ans.traversal(nodeA)