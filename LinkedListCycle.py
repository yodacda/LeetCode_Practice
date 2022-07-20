class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        #declare two pointers slow and fast, slow will shift one node at a time, fast will shift two nodes at a time.
        # if its has cycle it will meet one point, then return true.
        # if fast has null value then return false
class solution:
    def hasCycle(head:ListNode):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False