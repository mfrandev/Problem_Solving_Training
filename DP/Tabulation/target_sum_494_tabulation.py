"""
Moving to 2D DP:
1. Seed dp[0][0] = 1 "There is 1 way to sum 0 with 0 elements"
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums) + 1
        dp = [defaultdict(int) for _ in range(n)]
        dp[0][0] = 1 
        for i in range(1, n):
            for s in dp[i-1]:
                dp[i][s + nums[i-1]] += dp[i-1][s] 
                dp[i][s - nums[i-1]] += dp[i-1][s] 
        return dp[-1][target]
            
        
