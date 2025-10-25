# ========================== interval list intersections (leetcode 986) review ==========================
"""
1. Lists A and B are not merged.
2. Will need to check if there is any overlap or not.
3. If no overlap, then need to move up the lagging interval.
4. If overlap, then determine how the overlap works. i.e., does first interval or second interval start denote overlap?
5. Same issue for end.
"""

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        solution = []
        while i < len(firstList) and j < len(secondList):
            first_start, first_end = firstList[i][0], firstList[i][1]
            second_start, second_end = secondList[j][0], secondList[j][1]
            if first_end < second_start:
                i += 1
                continue
            elif second_end < first_start:
                j += 1
                continue
            if first_start < second_start:
                if first_end < second_end:
                    solution.append([second_start, first_end])
                    i += 1
                else:
                    solution.append([second_start, second_end])
                    j += 1
            else: # second_start <= first_start
                if second_end < first_end:
                    solution.append([first_start, second_end])
                    j += 1
                else:
                    solution.append([first_start, first_end])
                    i += 1
        return solution

# ========================== merge intervals (leetcode 56) ==========================
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
    
# ========================== minimum number of arrays to burst balloons (leetcode 452) ==========================
"""
Fact 1: Input points is a list of balloons whose diameter falls along the x-axis.
Fact 2: Arrows are shot directy upwards, pop all balloons in path, and do not pop any on the way down.
Fact 3: We are minimizing the number of arrows that must be shot to burst all balloons. 

Observation 1: We can't change the diameter of baloons so we are essentially counting the number of overlap occurences. 
Observation 2: We will need to sort by starting point. 
Obseravtion 3: We want to grab all balloons whose start is <= to the earliest balloon's endpoint.
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda point: point[0])
        solution = 0
        points_index = 0
        while points_index < len(points):
            _, soonest_point_end = points[points_index]
            while points_index < len(points) and points[points_index][0] <= soonest_point_end:
                soonest_point_end = min(soonest_point_end, points[points_index][1])
                points_index += 1
            solution += 1
        return solution

# ========================== non-overlapping intervals (leetcode 435) ==========================
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