# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        itr = head

        while itr:
            length += 1
            itr = itr.next
        
        itr = head
        prev = None
        for i in range(length - n):
            prev = itr
            itr = itr.next

        if not prev:
            next = itr.next
            itr.next = None
            return next
        
        prev.next = itr.next
        itr.next = None
        return head