# Fact 1: We are looking for maximum
# Fact 2: We will always have a solution 

# Observation 1: This doesn't look like a sort solution. (So O(n) is target)
# Observation 2: Volume of container for a given section is limited by min(nums[i], nums[j])
# Observation 3: We generally like higher barriers than shorter ones
# Observation 4: Two pointers looks good here

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        sol = (right - left)  * (min(height[left], height[right]))
        while left < right:
            sol = max(sol, (right - left)  * (min(height[left], height[right])))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return sol
