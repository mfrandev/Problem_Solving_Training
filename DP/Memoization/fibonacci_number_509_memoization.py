"""
Definition of fib: 
{
| fib(1) or fib(2): 1
| fib(n): fib(n - 1) + fib(n - 2)
}
"""

class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def search(num):
            if num <= 0:
                return 0
            if num == 1 or num == 2:
                return 1
            if num in memo:
                return memo[num]
            memo[num] = search(num - 1) + search(num - 2)
            return memo[num]
        return search(n)
