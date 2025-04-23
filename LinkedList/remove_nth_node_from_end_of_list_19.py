# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Observation 1: This problem feels like a stack problem.
Observation 2: The second approach would be a recursive solution.
Observation 3: The reason why this feels like a stack/recursion problem is because it's n nodes "FROM THE END."
Observation 4: Need some case to cover removing head from the list.

Stack Approach:
1. Iterate through the linked list, and add each element to the stack.
2. Pop n times from the stack, saving the previously popped value. The nth node popped is the node to remove.

"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        it = head
        while it:
            stack.append(it)
            it = it.next

        continuation_node = None
        current = None
        for i in range(n):
            continuation_node = current
            current = stack.pop()
        
        # If we are supposed to remove the first element of the list, return the second element of the list
        if not stack:
            return continuation_node
            
        # We want to remove current from the list
        node_before_node_to_remove = stack.pop()
        node_before_node_to_remove.next = continuation_node

        return head
