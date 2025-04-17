def minCostClimbingStairs(self, cost):
    if cost == 0:
        return 0
    if cost < 3:
        return min(cost[0], cost[1])
    cost_len = len(cost)
    dp = [0] * (cost_len)
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, cost_len):
        dp[i] = min(dp[i-1], dp[i-2]) + cost[i] # Recurrence relation: Always need to pay for the cost at the current step, but should have stepped one or two to get here ? 
    return min(dp[cost_len-2], dp[cost_len-1])
