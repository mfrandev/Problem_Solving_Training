# Fact 1: [2, 3, 2] and [2, 2, 3] count as the same list

# Observation 1: Since we are not generating permutations, we don't want a branching factor of n. 
# Observation 2: The only actions we have are to include the current number in the sum thus far, or not to include it. I.e., branching factor of 2.
# Observation 3: We need a success runway and failure runway

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def search(total, index, arr):
            if total > target or index >= len(candidates):
                return
            if total == target:
                res.append(arr[:])
                return
            arr.append(candidates[index])
            search(total + candidates[index], index, arr)
            arr.pop()
            search(total, index + 1, arr)
        search(0, 0, [])
        return res
