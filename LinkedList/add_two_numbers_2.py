# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Observation 1: First element of the linked list is the LSD of the value.
Observation 2: The sums of two values can exceed 10. Need to track a carry throughout the calculation

Comment 1: Although I solved the problem bottom-up using a stack, I don't know how to construct to results set top-down. Need to learn that.
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_it = l1
        l2_it = l2
        active_carry = 0
        solution_stack = []
        while l1_it and l2_it:
            l1_l2_active_carry_sum = l1_it.val + l2_it.val + active_carry
            active_carry, value = 0, l1_l2_active_carry_sum
            if l1_l2_active_carry_sum >= 10:
                active_carry = l1_l2_active_carry_sum // 10
                value = l1_l2_active_carry_sum % 10
            solution_stack.append(value)
            l1_it = l1_it.next
            l2_it = l2_it.next
        while l1_it:
            l1_active_carry_sum = l1_it.val + active_carry
            active_carry, value = 0, l1_active_carry_sum
            if l1_active_carry_sum >= 10:
                active_carry = l1_active_carry_sum // 10
                value = l1_active_carry_sum % 10
            solution_stack.append(value)
            l1_it = l1_it.next
        while l2_it:
            l2_active_carry_sum = l2_it.val + active_carry
            active_carry, value = 0, l2_active_carry_sum
            if l2_active_carry_sum >= 10:
                active_carry = l2_active_carry_sum // 10
                value = l2_active_carry_sum % 10
            solution_stack.append(value)
            l2_it = l2_it.next

        if active_carry > 0:
            solution_stack.append(active_carry)
        
        solution_head = None
        while solution_stack:
            val = solution_stack.pop()
            solution_node = ListNode(val, solution_head)
            solution_head = solution_node
        
        return solution_head
