class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeLinkedLists(self, l1:ListNode, l2:ListNode):
        dummy = ListNode()
        tail = dummy

        # traverse l1 and l2 nodes till not null
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next


list1 = [1,2,4]
list2 = [1,3,4]
sol = Solution()
sol.mergeLinkedLists(list1, list2)