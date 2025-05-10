"""
Am I literally doing what the problem says, or am I simulating what the problem says ? Likely, we don't want to start modifying the nums array.

Point 1: Earning nums[i] only deletes all nums[i] + 1 and nums[i] - 1. Not all nums[i]!

Can "flatten" each value by summing all occurances of it 
"""

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        mapping = defaultdict(int)
        for n in nums:
            mapping[n] += n
        sorted_keys = list(mapping.keys())
        sorted_keys.sort()
        values = [mapping[k] for k in sorted_keys]
        if len(values) == 1:
            return values[0]
        prev = values[0]
        if sorted_keys[1] - sorted_keys[0] == 1:
            curr = max(values[0], values[1])
        else:
            curr = values[0] + values[1]
        for i in range(2, len(values)):
            skip = curr
            if sorted_keys[i] - sorted_keys[i - 1] == 1:
                rob = prev + values[i]
            else:
                rob = curr + values[i]
            temp_max = max(rob, skip)
            prev, curr = curr, temp_max
        return curr
