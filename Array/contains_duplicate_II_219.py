# Observation 1: We want to minimize abs(i - j) so < k, so we want to bias the first occurance of a number in the array.

# Correction 1: We don't want to bias the first occurance, we want to bias the MOST RECENT occurance!

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}

        for i, n in enumerate(nums):
            if n not in map:
                map[n] = i
            elif nums[map[n]] == nums[i]:
                dist = abs(map[n] - i)
                if dist <= k:
                    return True
                map[n] = i

        return False
