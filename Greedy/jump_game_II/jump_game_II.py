"""
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

Rule 1: 0 <= j <= nums[i] 
    - nums[i] tells you the maximum length jump we can take. We don't need to take the maximum jump length.
    - In fact, the optimal jump length may not be the maximum..

Rule 2: i + j < n
    - "We cannot jump out-of-bounds."
    - Worth mentioning, that we won't get negative values for nums[i], so no need to worry about the -1 lower bound.

Constraint 1: We might have up to 10^4 n.
    - Should be solving in O(n) time
Constraint 2: No jumps greater than 1000.
Constraint 3: We are guaranteed a solution exists.

Observation 1: We are trying to reach the [n-1]th index.
Observation 2: We can jump from i-to-j, if j - nums[j] <= i.
Observation 3: We are looking for a minimum value.
Observation 4: If nums[i] == 0, we are stuck

Approach point 1: We want to start at the end of the input, take the last element, "move the goalpost back" by that many positions. 
Approach point 2: At each step while moving back the goalpost, find the minimum value for j - nums[i].

Implementation issue 1: What implied that this problem is bi-directional ? We do in fact need to start at the start and end at the end.

Bad Approach. Trying again.

Invariant: What is/store the highest index in the array we can reach from each point in the array, given the information we have so far?
Answer: max(farthest, i + nums[i])

"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        num_jumps = 0
        current_position = 0
        farthest_possible_position_from_current = 0
        for i in range(n - 1):
            if current_position >= n - 1:
                    break
            # This is the invariant. Note how we use a max function to determine it.
            farthest_possible_position_from_current = max(farthest_possible_position_from_current, i + nums[i])

            # If we've reached the best possible position we can get to so far, then update and increment jump
            if i == current_position:
                current_position = farthest_possible_position_from_current
                num_jumps += 1

        return num_jumps
