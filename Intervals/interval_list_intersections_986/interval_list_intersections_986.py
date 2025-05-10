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
