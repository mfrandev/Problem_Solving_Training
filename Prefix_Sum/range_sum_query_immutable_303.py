# Observation 1: We are calculating an index bounded sum in an array, so we will use prefix-sum
# (Prefix sum means the sum between i and j is p[j] - p[i-1])

# Observation 2: If left is 0 to begin with, we will subtract 0 from p[j]

class NumArray:

    nums = []
    p = []

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.p = [self.nums[0]]
        for i in range(1, len(nums)):
            self.p.append(self.p[i-1] + self.nums[i])


    def sumRange(self, left: int, right: int) -> int:
        return self.p[right] - (0 if left == 0 else self.p[left - 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
