class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def search(index, goalpost, memo):
            if index == len(nums):
                if goalpost == 0:
                    return 1
                else:
                    return 0
            if (index, goalpost) in memo:
                return memo[(index, goalpost)]
            memo[(index, goalpost)] = search(index + 1, goalpost + nums[index], memo) + search(index + 1, goalpost - nums[index], memo)
            return memo[(index, goalpost)]
        return search(0, target, memo)
