# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Observation 1: If a linked list has a cycle, that means a slow pointer will eventually reach a faster pointer in the traversal, if the fast pointer moves twice as quickly 
# Observation 2: The head can be null, so that is trivially false
# Observation 3: If the fast pointer, or its next element, is ever null then there is no cycle (i.e., end of list)
# Observation 4: The fast and slow pointer cannot be initialized at the same position

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        fast, slow = head.next, head
        while fast != None and fast.next != None:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False
