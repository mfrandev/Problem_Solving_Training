# Observation 1: We get duplicates when we recurse on the same value in the same depth of the call stack

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, subset = [], []
        def dfs(i):
            if i == len(nums):
                subsets.append(subset[:])
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i + 1)
        dfs(0)
        return subsets
