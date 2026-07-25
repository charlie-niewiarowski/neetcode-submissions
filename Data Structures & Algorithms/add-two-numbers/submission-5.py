# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            value = l1.val + l2.val + carry
            carry = 1 if value >= 10 else 0

            curr.next = ListNode()
            curr.next.val = value % 10

            l1, l2, curr = l1.next, l2.next, curr.next

        while l1:
            value = l1.val + carry
            carry = 1 if value >= 10 else 0

            curr.next = ListNode()
            curr.next.val = value % 10

            l1, curr = l1.next, curr.next

        while l2:
            value = l2.val + carry
            carry = 1 if value >= 10 else 0

            curr.next = ListNode()
            curr.next.val = value % 10

            l2, curr = l2.next, curr.next
        
        if carry == 1:
            curr.next = ListNode()
            curr.next.val = 1
        
        return dummy.next



