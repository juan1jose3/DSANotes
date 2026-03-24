class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1)
nodeB = ListNode(2)
nodeC = ListNode(2)
nodeD = ListNode(1)

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = None

class Solution:
    def isPalindrome(self,head) -> bool:
        current_node = head
        val_list = []

        while current_node:
            val_list.append(current_node.val)
            current_node = current_node.next

        return val_list == val_list[::-1]

ans = Solution()
print(ans.isPalindrome(head))