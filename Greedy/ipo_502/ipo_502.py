"""
Fact 1: can finish at most k distinct projects.

Observation 1: More projects is better than fewer projects, unless some project has value <= 0.
Observation 2: If we cannot make any more projects, then we are done!
Observation 3: We cannot sort, because the mapping from capital to profits is broken.
Observation 4: We can zip the lists together, and sort by the capital requirement.
Observation 5: We can then add only the projects we can build currently, then take the best one.
"""

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pairs = []
        for i in range(len(profits)):
            pairs.append((capital[i], profits[i]))
        pairs.sort(key = lambda p: p[0])
        i = 0
        max_capital = []
        while k > 0:
            while i < len(pairs) and pairs[i][0] <= w:
                heapq.heappush(max_capital, -pairs[i][1])
                i += 1
            if not max_capital:
                break
            w -= heapq.heappop(max_capital)
            k -= 1
        return w
