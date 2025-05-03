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

