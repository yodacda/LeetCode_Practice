class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class solution:
    def removeNthFromEnd(head:ListNode, n):
        dummy = ListNode(0, head)
        left = dummy
        right = head

        #find out the right starting point in a Node
        while n > 0 and right:
            right = right.next
            n -= 1

        #Traverse the whole list
        while right:
            left = left.next
            right = right.next

        #delete the node
        left.next = left.next.next
        return dummy.next
    