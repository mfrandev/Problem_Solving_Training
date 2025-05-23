# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev, curr, nxt = None, head, head.next
        while curr is not None:
            curr.next = prev
            prev = curr
            curr = nxt
            if nxt is not None:
                nxt = nxt.neaxt
        return prev
