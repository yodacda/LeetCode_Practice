class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


###Do not return anything, modify head in-place instead.
class Solution:
    def reOrderList(head:ListNode):
        slow, fast = head, head.next
        #finding the length of input linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse the second half
        second = slow.next
        prev = None
        slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        #merge two lists
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


