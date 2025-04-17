# Observation 1: 0-indexing implies that we should set our boundries as [0, n], rather than [0, n - 1]
# Observation 2: Given this, we set left to mid + 1 when looking for a larger value.
# Observation 3: We will set right to mid when looking for a smaller value.
# Observation 4: At the end of this loop, 'l' is the minimal 'i' which satisfies our condition.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m
        return -1
