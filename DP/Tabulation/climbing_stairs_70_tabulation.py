"""
N stairs in the staircase. How many DISTINCT ways can we get there. Not best/worst. DISTINCT

We can take one or two steps at each point
- Branching factor of 2.
- From step k, there are n ways to get to the top

If we are at the top, or over the top, there is nothing we can do
If there is 1 step to go, we have one way
If there are 2 steps to go, there are two ways (1+1, 2)

If we have 3 steps to go, we can either take 1 step, or we can take two seps. 1 step gets us to the 2nd to last step (2) and 2 steps gets us to the last step (1) so num(2) + num(1) is good.

If we have k steps to go, we can either take 1 step to the k-1th step, or 2 steps to the k-2th step. We would have ways(k-1) + ways(k-2) ways of getting to the destination from the kth step.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        solution = [0] * (max(3, n + 1))
        solution[1], solution[2] = 1, 2
        for i in range(3, n + 1):
            solution[i] = solution[i - 1] + solution[i - 2]
        return solution[n]
