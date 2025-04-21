# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Observation 1: Do a DFS, track the minimum depth of each branch
# Observation 2: If either of the left or right subtrees returns 0, take a maximum because we are looking for leaf nodes.

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        # I.e., not a leaf node.
        if(left == 0 or right == 0):
            return max(left, right) + 1
        return min(right, left) + 1
