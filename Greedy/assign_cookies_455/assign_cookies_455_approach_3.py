"""
Approach 3 (NeetCode):
Observation 1: The number of kids we satisfied is the same as the end position of gp (we don't even need to track solution).
Observation 2: Sorting means that elements at the start of g will match with the elements at the start of s.
Observation 3: Since cookies and greediness values are both monotonically increasing, we won't need to undo any of our actions (so greedy).
"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # If either list empty, base case
        g.sort()
        s.sort()
        gp = sp = 0
        while gp < len(g) and sp < len(s):
            if g[gp] <= s[sp]:
                gp += 1 
                sp += 1
            else:
                sp += 1
        return gp
