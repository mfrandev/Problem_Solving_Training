def minSubArrayLen(self, target, nums):
    # Looking for the smallest subarray size whose sum is greater than or equal to target
    l = 0
    smallest = len(nums) + 1 # Initialize smallest as an impossible solution
    current_sum = 0 # Keep track of the sum of subarray in 0(1)
    for i in range(len(nums)):
        current_sum += nums[i] # Get sum of new window
        while current_sum >= target: # If we've encountered a possible solution, iterate until no longer a solution
            smallest = min((i-l+1), smallest) # Check if this solution is an optimal one
            current_sum -= nums[l]
            l += 1
    return 0 if smallest > len(nums) else smallest # If we've never left the impossible solution state, then we have none