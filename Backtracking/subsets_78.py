# Observation 1: Each subsequent recursive call represents the next index in the input array
# Obsercation 2: There are two possible actions: Add the element to the solution array or do not add the element to the solution array

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, solution = [], [] 
        n = len(nums)
        def search(depth):
            if n == depth:
                result.append(solution[:])
                return
            # Action 1: We do not add the element to the solution
            search(depth+1)
            # Action 2: We do add the element to the solution
            solution.append(nums[depth])
            search(depth+1)
            solution.pop()
        search(0)
        return result
