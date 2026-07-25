# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        dummy = ListNode()
        curr = dummy

        while True:
            minNode = None
            minIdx = -1
            for i in range(0, len(lists)):
                if not lists[i]:
                    continue
                if not minNode or lists[i].val < minNode.val:
                    minNode = lists[i]
                    minIdx = i

            if not minNode:
                return dummy.next
            curr.next = minNode
            curr = curr.next
            lists[minIdx] = lists[minIdx].next


