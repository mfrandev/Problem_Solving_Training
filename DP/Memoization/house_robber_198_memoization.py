def rob(self, nums):

        memo = {}  # Initialize the memoization table
        
        def getAns(i):
        
            if i < 0: # Base case, don't leave the search space-
                return 0
                
            if i in memo: # If solution is cached already, return it
                return memo[i]
                
            result = max(getAns(i-2) + nums[i], getAns(i-1)) # Recurrence relation: Either rob this house and the one two before it, or the previous house
            
            memo[i] = result
            return result
            
        getAns(len(nums)-1)
        return memo[len(nums)-1]
