# Fact 1: input is a string-rep of an integer, and a constraint for values to remove from that string
# Fact 2: Solutions should not contain leading zeros

# Observation 1: All possible non-trival/error solutions are of the same length: (len(str) - k)
# Observation 2: Problem can be reduced to "After removing 'k' chars, produce the lexicographically smallest string." Should maintain K as we make removals
# Observation 3: We are minimizing, so we like smaller numbers more than bigger numbers, in general.
# Observation 4: We want to make sure that the monotonic increasing order (rembember base 10!)
# Observation 5: We want to bias smaller digits that are more significant (i.e., arr should be increasing)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for d in num:
            while k > 0 and stack and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
        stack = stack[:len(stack) - k]
        start = 0
        while len(stack) > start and stack[start] == "0":
            start += 1
        res = "".join(stack[start:])

        return res if res else "0"
            
