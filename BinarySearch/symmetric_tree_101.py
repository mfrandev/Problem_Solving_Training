# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Observation 1: There is nothing stopping from traversing both branches at the same time!!!
# Observation 2: If that's the case, then this is simply writing a recursive definition of a symmetric tree!! 

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and isMirror(left.right, right.left) and isMirror(left.left, right.right)
        return isMirror(root.left, root.right)
            
