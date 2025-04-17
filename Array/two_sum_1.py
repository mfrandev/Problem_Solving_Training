# Observation 1: We want to map target numbers to the indicies. I.e., if target is 9 and we see a 7 at index i, insert {2: i} into the map. This means if we find a 2, it pairs with the value at index i.  

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if num not in map:
                map[diff] = i
            else:
                return [map[num], i]
