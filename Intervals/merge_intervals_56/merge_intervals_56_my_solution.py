"""
As with the previous interval problem, we will detect interval overlap by sorting by end point, then checking prev_end vs curr_start. If there is an overlap, we will make a new interval [prev_start, curr_end]. If there is no overlap, we simply add the interval to the list. 

Note: We will always have at least one interval. 

"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[1])
        solution = [[intervals[0][0], intervals[0][1]]]
        # print(f'Sorted intervals: {intervals}')
        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i][0], intervals[i][1]
            prev_start, prev_end = solution[-1][0], solution[-1][1]
            if current_start > prev_end:
                solution.append([current_start, current_end])
            else:

                # Purpose of this while loop is to get the "next" interval in current_start, current_end
                while solution and current_start <= prev_end:
                    pop_start, pop_end = solution.pop()
                    if current_start <= pop_end:
                        current_start, current_end = min(current_start, pop_start), max(current_end, pop_end)
                    if solution:
                        prev_start, prev_end = solution[-1][0], solution[-1][1]
                solution.append([current_start, current_end])
        return solution
