"""
Much simpler solution is to sort by starting point, then update the end point of any intervals with clashes. This means there is no need for a while loop to go back and re-merge the current interval with the popped interval. 
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        solution = [[intervals[0][0], intervals[0][1]]]
        for interval in intervals:
            if interval[0] > solution[-1][1]:
                solution.append(interval)
            else:
                solution[-1][1] = max(solution[-1][1], interval[1])
        return solution
