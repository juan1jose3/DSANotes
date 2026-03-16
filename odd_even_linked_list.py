class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


head = ListNode(2)
nodeB = ListNode(1)
nodeC = ListNode(3)
nodeD = ListNode(5)
nodeE = ListNode(6)
nodeF = ListNode(4)
nodeG = ListNode(7)


head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF
nodeF.next = nodeG
nodeG.next = None




class Solution:
    def oddEvenList(self, head:ListNode):
        index = 1
        prev_node = None
        current_node = head
        odd_list = ListNode()
        odd_head = odd_list


        even_list = ListNode()
        even_head = even_list


        while current_node:
            if index == 1 and current_node.next == None:
                return current_node
            if index % 2 != 0 or index == 1:
                odd_list.next = current_node
                odd_list = odd_list.next
            elif index % 2 == 0:
                even_list.next = current_node
                even_list = even_list.next

            index += 1
            if current_node.next == None:
                if index % 2 == 0:
                    prev_node.next = None
                elif index % 2 != 0:
                    prev_node.next = None
                    
            prev_node = current_node
            current_node = current_node.next

        odd_list.next = even_head.next
        return odd_head.next

   



    def traversal(self,head):
        current_node = head
        while current_node:
            print(current_node.val)
            current_node = current_node.next


ans = Solution()
newHead = ans.oddEvenList(head)
ans.traversal(newHead)