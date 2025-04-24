# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
1 2 3 4 5 : k = 2 -> 4 5 1 2 3
Observation 1: The last k elements should be moved to the front of the list, preserving order.
Observation 2: The rest of the list should be preserved, but not cycle back to the len(list) - kth element.
Observation 3: k has the constraint 0 <= k <= 2 * 10^9. This obviously means that we can end up cycling more times than necessary. It would be wise to get the length of the list, and update k to be [k mod len(list)]
Observation 4: We will not have more than 500 nodes in the list, so we can comfortably store them in a stack.
"""

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Edge cases
        if not k or not head:
            return head

        it = head
        stack = []

        # 1. Fill the stack
        while it:
            stack.append(it)
            it = it.next

        # 2. Update K to avoid unnecessary work
        k = k % len(stack)
        if k == 0:
            return head

        # 3. Get the final k elements in order. Set head_of_rotated_segment to initially be head, because that should come immediately following the last rotated element.
        head_of_rotated_segment = head
        for i in range(k):
            top = stack.pop()
            top.next = head_of_rotated_segment
            head_of_rotated_segment = top

        # 4. Remove the cycle from the linked list. The next element at the top of the stack should be the last element of the solution.
        top = stack.pop()
        top.next = None
        return head_of_rotated_segment
