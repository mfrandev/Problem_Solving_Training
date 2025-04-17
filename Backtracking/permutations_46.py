# Observation 1: We have n! number of permutations, where n = len(nums)
# Observation 2: Recursive base case: Permutation of nothing is [[]]
# Observation 3: Subproblems are to add the novel element at each position of the array.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        permutations = self.permute(nums[1:])
        result = []
        for p in permutations:
            for i in range(0, len(p) + 1):
                copy = p[:]
                copy.insert(i, nums[0])
                result.append(copy)
        return result

# Iterative solution, very similar
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         perms = [[]]

#         for n in nums:
#             new_perms = []
#             for p in perms:
#                 for i in range(0, len(p) + 1):
#                     copy = p[:]
#                     copy.insert(i, n)
#                     new_perms.append(copy)
#             perms = new_perms
#         return perms
