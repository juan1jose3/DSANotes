class ListNode:
    def __init__(self,val=0, next=None) -> None:
        self.val = val
        self.next = next

    


head = ListNode(1)
nodeA = ListNode(2)
nodeB = ListNode(3)
nodeC = ListNode(4)


head.next = nodeA
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = None