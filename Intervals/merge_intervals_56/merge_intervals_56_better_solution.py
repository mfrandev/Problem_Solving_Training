"""
Much simpler solution is to sort by starting point, then update the end point of any intervals with clashes. This means there is no need for a while loop to go back and re-merge the current interval with the popped interval. 
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda p:p[0])
        res=[]
        for l,r in intervals:
            if not res or l > res[-1][1]:
                res.append((l,r))
            else:
                res[-1]=[min(l, res[-1][0]), max(r, res[-1][1])]
        return res