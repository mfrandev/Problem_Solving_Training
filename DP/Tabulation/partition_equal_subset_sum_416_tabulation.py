class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        dp = set()
        dp.add(0)
        for i in range(1, len(nums)):
            temp_set = set()
            for c in dp:
                temp = c + nums[i - 1]
                if temp == target:
                    return True
                temp_set.add(temp)
                temp_set.add(c)
            dp = temp_set
        return False


