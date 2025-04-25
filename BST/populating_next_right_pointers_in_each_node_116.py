"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

"""
Observation 1: Based on the figure, we are doing a level-order traversal. The last element on each level should point to null.
Observation 2: This is a bit like a linked list and tree structure in one. We can level order traversal, place each element in a given level in a stack, and reconstruct the linked list.
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q = deque()
        q.append(root)
        while q:
            level_length = len(q)
            level_stack = []
            for i in range(level_length):
                node = q.popleft()
                level_stack.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            next_in_level = None
            while level_stack:
                top = level_stack.pop()
                top.next = next_in_level
                next_in_level = top
        return root

