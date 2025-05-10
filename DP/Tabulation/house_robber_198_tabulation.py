class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        prev, curr = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            new_max = max(nums[i] + prev, curr)
            prev = curr
            curr = new_max
        return curr