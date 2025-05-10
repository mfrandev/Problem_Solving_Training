"""

"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def search(index):
            if index >= len(cost):
                return 0
            if index in memo:
                return memo[index]
            memo[index] = min(search(index + 1), search(index + 2)) + cost[index]
            return memo[index]
        return min(search(0), search(1))
