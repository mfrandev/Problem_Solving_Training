# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
We will iterate through the linked list. Once we hit a duplicate, we iterate until finding a new element. Then continue until finishing the process.

Comment: Neglected to vocalize the state of "it" when the inner while terminates. This would have avoid the error of having head.next = it, instead of the correct head.next = it.next.
"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        while head:
            it = head
            while it.next and it.val == it.next.val:
                it = it.next
            head.next = it.next
            head = head.next
        return dummy.next
