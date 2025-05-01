"""
1. Input: List of tuples, [start, end] for an interval.
2. Output: Number, representing minimum number of intervals we need to remove to make 0 overlaps.
3. All intervals are of the form [start, end)

Observation 1: If we sort the intervals, we can see if two consecutive intervals interlap by checking if the [i+1]st interval starts before the ith ends. Because we sorted, we want to remove the [i+1], since it is larger and has less potential for future overlap.

Observation 2: The intervals line up after sorting far more nicely if we sort by the ending value. In python, we do arr.sort(key = lambda x: x[1]) to do that. The 'x' in the lambda function is the same object shape as each element of the array.
- This produces [[1,2],[2,3],[1,3],[3,4]], instead of [[1,2],[1,3],[2,3],[3,4]]

"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        prev_end = intervals[0][1]
        solution = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start < prev_end:
                solution += 1
            else:
                prev_end = end
        return solution
