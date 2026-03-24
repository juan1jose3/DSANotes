class ListNode:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next


nodeA = ListNode(1)
nodeB = ListNode(2)
nodeC = ListNode(3)
nodeD = ListNode(4)
nodeE = ListNode(5)


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

    def reverseList(self,head):
        current_node = head
        next_node = None
        prev_node = None

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        head = prev_node
        return head

ans = Solution()

new_head = ans.reverseList(nodeA)
ans.traversal(new_head)