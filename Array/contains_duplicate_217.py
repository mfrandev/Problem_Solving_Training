# Observation 1: Set data structure does not allow duplicates, so if len(set(array)) == len(array), no duplicates

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
