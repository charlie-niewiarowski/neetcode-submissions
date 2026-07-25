# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find tail of first half
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        c2, p2 = slow.next, slow
        slow.next = None

        while c2:
            next = c2.next
            c2.next = p2
            p2 = c2
            c2 = next
        
        # merge
        c1 = head
        c2 = p2

        while c2 != slow:
            n1, n2 = c1.next, c2.next
            c1.next = c2
            c2.next = n1
            c1, c2 = n1, n2
            
