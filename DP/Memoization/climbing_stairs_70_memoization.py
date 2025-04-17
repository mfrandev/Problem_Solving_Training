def climbStairs(self, n):
    memo = {}
    def climb(i):
        if i < 0:
            return 0
        if i == 1:
            return 1
        if i == 2:
            return 2
        if i in memo:
            return memo[i]
        memo[i] = climb(i - 1) + climb(i - 2)
        return memo[i]
    return climb(n)
