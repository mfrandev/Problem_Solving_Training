# Observation 1: Can use a prefix sum mapping, where 1's add 1 to sum, 0's add -1 to sum.
# Observation 2: Looking for 0-values in that prefix sum array, or ranges where p[i] - p[j] = 0
# Observation 3: Keep a dictionary where the particular sum is mapped to the index of first occurance
# Observation 4: Maintain a max length where either condition in observation 2 holds.

# Comment 1: This solution was accepted, but very inefficient. 
# Comment 2: The approach was on the correct complexity scale though, 3-passes of 0(n), so O(n)
# Comment 3: We don't need to iterate three times. That fixes the runtime issue. 

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        votes = 0 # This will be positive if more 1s than 0s, else negative
        result = 0
        d = {}
        for i, n in enumerate(nums):
            # First, vote
            if n == 0:
                votes -= 1
            else:
                votes += 1
            
            # Second, we need to keep the index this vote count first appears at
            if votes not in d:
                d[votes] = i

            # Third, if votes are 0, this case is a guaranteed greedy maximum
            if votes == 0:
                result = i + 1
            elif votes in d:
                result = max(result, i - d[votes])

        return result

