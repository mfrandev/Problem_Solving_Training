# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# Observation 1: isBadVersion(int) is our "condition function"

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        while l < r:
            m = l + (r - l) // 2
            if not isBadVersion(m):
                l = m + 1
            else:
                r = m 
        return l 

