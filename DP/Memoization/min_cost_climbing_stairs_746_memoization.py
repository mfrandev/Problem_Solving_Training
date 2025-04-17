def minCostClimbingStairs(self, cost):
    memo = {}
    def getAns(i):
        if i == (len(cost) - 2) or i == (len(cost) - 1):
            return cost[i]
        if i >= len(cost):
            return 0
        if i in memo:
            return memo[i]
        memo[i] = min(getAns(i + 1), getAns(i + 2)) + cost[i]
        return memo[i]
    return min(getAns(0), getAns(1))
