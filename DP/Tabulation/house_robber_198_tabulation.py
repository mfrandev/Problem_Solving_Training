# Optimized approach using 2 variables, prev and curr, in place of a "dp" array
def rob(self, nums):
    if len(nums) == 1:
        return nums[0]
    prev = nums[0]
    curr = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        prev, curr = curr, max(curr, prev + nums[i])
    return curr
    
# Base solution using "dp" array
# def rob(self, nums):
#     if len(nums) == 1:
#         return nums[0]
#     dp = [0] * len(nums)
#     dp[0] = nums[0]
#     dp[1] = max(nums[0], nums[1])
#     for i in range(2, len(nums)):
#         dp[i] = max(dp[i-1], dp[i-2] + nums[i])
#     return dp[len(nums)-1]
