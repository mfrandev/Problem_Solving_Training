# Observation 1: Matches can be placed in either the top, right, bottom, or left. I.e., branching factor of 4
# Observation 2: All sides square must be equal length, and must use all matches. Thus, sum(arr) / 4 is length of each side.
# Observation 3: It's possible that sum(arr) / 4 is not an integer, can return False early in this case 
# Observation 4: If array contains any elements greater than a side length, can return False early
# Observation 5: 

# Note 1: Array sort is in-place

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        # Reverse sort for observation 4
        matchsticks.sort(reverse=True)

        # Observation 2
        target_side_length = sum(matchsticks) // 4

        # Observation 4
        if matchsticks[0] > target_side_length:
            return False

        # Observation 3
        if target_side_length != sum(matchsticks) / 4:
            return False

        sides = [0] * 4
        
        # This function returns a value. We will need to check that value in the recursion stack
        def backtrack(pos):
            if pos == len(matchsticks):
                return True
            for i in range(len(sides)):
                if (sides[i] + matchsticks[pos]) <= target_side_length:
                    sides[i] += matchsticks[pos]
                    if backtrack(pos + 1):
                        return True
                    sides[i] -= matchsticks[pos]

                # WTF is going on here
                if sides[i] == 0 or sides[i] + matchsticks[pos] == target_side_length:
                    break    
            return False
 

        return backtrack(0)
