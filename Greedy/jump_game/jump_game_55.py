"""
This is a "moving goalpost" problem. Essentially, we start from the "goal" of the last index, and we check for each index from the end if we can reach the "goal" from that index if we jump nums[i] number of positions. If we can, we move the goalpost to that position.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal <= 0
