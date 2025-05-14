"""
Is there a way to partition the array to meet some condition? 
NOT ASKING return the partition.

Must break the array into two subsets. Not more than 2.
We can either add the element to partition 1, or partition 2

We can memoize using the collection of "2 sums" as a key (sum1, sum2) since this uniquely defines state.

Doesn't even matter actually. Only must keep track of "sum" and "index."
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        memo = {}

        def can_partition(index, running_sum):
            if running_sum == target:
                return True
            if index == len(nums) or running_sum > target:
                return False
            if (index, running_sum) in memo:
                return memo[(index, running_sum)]
            if can_partition(index + 1, running_sum + nums[index]):
                memo[(index, running_sum)] = True
                return True
            if can_partition(index + 1, running_sum):
                memo[(index, running_sum)] = True
                return True
            memo[(index, running_sum)] = False
            return False
        
        return can_partition(0, 0)
            
