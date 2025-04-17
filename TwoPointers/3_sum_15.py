# Fact 1: Solution should continue unique triplets 
# Fact 2: Solution should contain the array values, not the indicies.
# Fact 3: Indicies must be unique, array values can be duplicated [0, 0, 0] is ok if i != j != k
# Fact 4: Values in the triplet must add up to 0
# Fact 5: There will be at least one valid triplet

# Observation 1: Do not see any monotonacity
# Observation 2: Order of output and order of triplets do not matter
# Observation 3: Can sort nums to get monotonacity
# Observation 4: Checking permutations where first or second element is the same will produce duplicates

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums = sorted(nums)
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[(i - 1)]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                temp_sum = nums[i] + nums[j] + nums[k]
                if temp_sum == 0:
                    solution.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif temp_sum > 0:
                    k -= 1
                else:
                    j += 1
        return solution
