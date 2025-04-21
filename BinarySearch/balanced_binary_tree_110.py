# Observation 1: abs(left - right) cannot exceed 1.
# Observation 2: Do a DFS, return the left/right subtree depths at each level and compare results with the invariant in observation 1.

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def search(node):
            if not node:
                return 0
            l = search(node.left)
            r = search(node.right)
            if abs(l - r) > 1:
                return float("inf")
            return max(l, r) + 1
        
        if not root:
            return True
        
        return abs(search(root.left) - search(root.right)) <= 1
