# Fact 1: An ugly number does not contain prime factors greater than 5.
# Fact 2: "1" is trivially considered to be an ugly number. 

# Observation 1: An ugly number is simply a composition of primes, where 2, 3, and 5 are the only valid options.
# Observation 2: We can derive ugly numbers by taking an element that we know is ugly and multiplying it by 2, 3, and 5. 
# Observation 3: By maintaining a heap data structure and an element count, we can find the nth ugly number.
# Observation 4: We need to track which elements we've seen to avoid duplicates.
# Observation 5: New ugly numbers are like the frontier of a graph.
# Observation 6: We are looking for nth element, which is index at n-1

# Building intuition:
# What exactly are the "actions" we can take at each step of the problem?
# What is the problem space?
# Are there any tools I know of that can be useful to search that space?

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        heapq.heapify(heap)
        factors = [2, 3, 5]
        visited = set()

        for i in range(n):
            current = heapq.heappop(heap)
            if i == n - 1:
                return current
            for f in factors:
                candidate = current * f
                if candidate not in visited:
                    heapq.heappush(heap, candidate)
                    visited.add(candidate)
