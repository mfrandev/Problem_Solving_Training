"""
Approach 1:
1. Min-heapify s and g
2. Pop from g to get the least greedy child.
3. Continuously pop from s until finally reaching a cookie >= child's greed.
4. Repeat steps 2 and 3 until there are either no cookies or no children.

Approach 1 Comments:
1. This is not an optimal solution complexity-wise. O([N Log N] + [M Log M])
2. This IS an optimal solution, memory-wise. O(1). 
3. Seems like the priority queue structure is making multiple appearances in greedy algorithm, which makes sense because it can help us make the most optimal choice at each iterative step.
"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        heapq.heapify(g)
        heapq.heapify(s)
        result = 0

        while g and s:
            smallest_childs_greed = heapq.heappop(g)
            while s: 
                smallest_cookie = heapq.heappop(s)
                if smallest_cookie >= smallest_childs_greed:
                    result += 1
                    break

        return result
