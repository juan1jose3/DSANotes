class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
#linked list 1


list_a_node_a = ListNode(4)
list_a_node_b = ListNode(1)

intersection = ListNode(8)



# Linked list 2

list_b_node_a = ListNode(5)
list_b_node_b = ListNode(6)
list_b_node_c = ListNode(1)

# shared 

shared_node_a = ListNode(4)
shared_node_b = ListNode(5)

list_a_node_a.next = list_a_node_b
list_a_node_b.next = intersection
intersection.next = shared_node_a
shared_node_a.next = shared_node_b
shared_node_b.next = None


list_b_node_a.next = list_b_node_b
list_b_node_b.next = list_b_node_c
list_b_node_c.next = intersection


class Solution:
    def getIntersectionNode(self,headA, headB):
        pointerA = headA
        pointerB = headB

        while pointerA != pointerB:
            
            if pointerA == None:
                pointerA = headB
            else:
                pointerA = pointerA.next

            if pointerB == None:
                pointerB = headA
            else:
                pointerB = pointerB.next

        if pointerA == pointerB:
            return f"Intersected at {pointerB.val}"
        
        return "No intersection"
    
    def traversal(self,head):
        current_node = head
        while current_node:
            print(current_node.val)
            current_node = current_node.next

ans = Solution()
print(ans.getIntersectionNode(list_a_node_a,list_b_node_a))