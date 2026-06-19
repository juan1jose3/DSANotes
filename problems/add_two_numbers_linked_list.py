class ListNode:
    def __init__(self,val=0, next=None) -> None:
        self.val = val
        self.next = next



headA = ListNode(2)
node_a = ListNode(4)
node_b = ListNode(3)

headA.next = node_a
node_a.next = node_b
node_b.next = None


headB = ListNode(5)
node_c = ListNode(6)
node_d = ListNode(4)


headB.next = node_c
node_c.next = node_d
node_d.next = None


class Solution:
    def addTwoNumbers(self, l1,l2):
        new_linked = ListNode()
        head = new_linked
        carry = 0
        pointer_a = l1 
        pointer_b = l2

        while pointer_a or pointer_b:
            
            actual_value_a = 0
            actual_value_b = 0

            if pointer_a == None:
                actual_value_a = 0
            else:
                actual_value_a = pointer_a.val
                pointer_a = pointer_a.next

            if pointer_b == None:
                actual_value_b = 0
            else:
                actual_value_b = pointer_b.val
                pointer_b = pointer_b.next
            
            num = actual_value_a + actual_value_b
            if carry > 0:
                num += carry 
                carry = 0
            if num > 9:
                n = num
                last = 0
                first = 0
                while n > 0:
                    last_digit = n % 10
                    n = n // 10

                    last = last_digit
                    first = n
                    break
                carry = first
                new_node = ListNode(last)
                new_linked.next = new_node
                
                new_linked = new_linked.next
                
            else:
                new_node = ListNode(num)

                new_linked.next = new_node
                new_linked = new_linked.next
            
        if carry > 0:
            new_node = ListNode(carry)
            new_linked.next = new_node

        return head.next
    
    def traversal(self, list):
        current_node = list
        while current_node:
            print(current_node.val)
            current_node = current_node.next
    


sol = Solution()
new_list = sol.addTwoNumbers(headA, headB)

sol.traversal(new_list)


    