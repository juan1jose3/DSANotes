class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

node1_list1 = ListNode(1)
node2_list1 = ListNode(2)
node3_list1 = ListNode(4)

node1_list1.next = node2_list1
node2_list1.next = node3_list1


node1_list2 = ListNode(1)
node2_list2 = ListNode(3)
node3_list2 = ListNode(4)

node1_list2.next = node2_list2
node2_list2.next = node3_list2


class Solution:
    def mergeTwoLists(self,list1, list2):
        merged_list = ListNode()
        merged_head = merged_list
        pointerA = list1
        pointerB = list2
      
        while pointerA and pointerB:
            
            
            if pointerA.val  <= pointerB.val:

                merged_list.next = pointerA
                pointerA = pointerA.next

            else:
                merged_list.next = pointerB
                pointerB = pointerB.next

            merged_list = merged_list.next
        if pointerA != None:
            merged_list.next = pointerA
        else:
            merged_list.next = pointerB
        return merged_head.next
            

    def traversal(self,list1):
        current_node = list1

        while current_node:
            print(current_node.val)
            current_node = current_node.next

ans = Solution()

merged_list= ans.mergeTwoLists(node1_list1,node1_list2)

ans.traversal(merged_list)
