"""
Approach 2:
1. We can sort the arrays, and work backwards.
2. If g[-1] <= s[-1], we can assign s[i] to g[i], and pop them both from respective array.
3. If g[-1] > s[-1], we pop from g, since there is no cookie that will satisfy that child.
4. Repeat steps 2 and 3 until there are no more cookies, or children. Number of cookies assigned will be the answer.
Ex: g: [7,8,9,10] s: [5,6,7,8]

"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # If either list empty, base case
        if not g or not s:
            return 0
        g.sort()
        s.sort()
        solution = 0
        while g and s:
            if g[-1] <= s[-1]:
                solution += 1
                g.pop()
                s.pop()
            else:
                g.pop()
        return solution
