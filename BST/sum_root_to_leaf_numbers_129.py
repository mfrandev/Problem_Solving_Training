# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each path from root to leaf represents a number. We want to get to each leaf node, record the number, and sum them all.

One approach may be to keep a string, and once at the leaf node (recursively), convert that string to an integer, then add it to the sum.

In this exercise, you learned that pass-by-value types become locally scoped in Python closures. For example, you cannot have a "sum" variable of type int and increment it from the search function. However, you CAN have an array of length 1, where arr[0] acts as an aggregator of the solution, which is what you've done here.
"""

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        arr = [0]
        def search(node, string):
            if not node:
                return
            string_at_this_level = string[:] + str(node.val)
            if not node.right and not node.left:
                arr[0] += int(string_at_this_level)
                return
            if node.left:
                search(node.left, string_at_this_level)
            if node.right:
                search(node.right, string_at_this_level)
            return

        search(root, "")
        return arr[0]
