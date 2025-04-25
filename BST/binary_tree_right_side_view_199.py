# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
This question just wants us to do a level-order traversal and add the last value of each level to a list. Then return that list.
"""

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        solution = []
        if not root:
            return solution
        q = deque()
        q.append(root)
        while q:
            length_of_level = len(q)
            for i in range(length_of_level - 1):
                elem = q.popleft()
                if elem.left:
                    q.append(elem.left)
                if elem.right:
                    q.append(elem.right)
            last = q.popleft()
            solution.append(last.val)
            if last.left:
                q.append(last.left)
            if last.right:
                q.append(last.right)
        return solution

