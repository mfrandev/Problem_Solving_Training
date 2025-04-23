"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Goal: Preserve information about the data in the sliding window as it moves.
1. Preserving the elements from the original array:
- Store the values themselves
- Store the indices
2. Preserving the order of elements
- Enforce a monotonic invariant on the data structure

[1, -1, 3, 2, -2, 5]

Observation 1: Q will never be greater than length k
Observation 2: We can maintain our Q, s.t. the element indexed by q[0] in nums is the greatest in the window (r - l + 1)
Observation 3: Whenever our window length policy (r - l + 1) is true, we have to do an action. In this case, add the largest element to the solution set.
Observation 4: Our stack clearing policy implies that the element at q[0] is not just the index of the largest element in window in (r - l + 1), but also the leftmost element we are storing. 

"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        solution = []
        q = deque()

        while r < len(nums):

            # While the element at the right of the window is bigger than all other elements
            while q and nums[r] > nums[q[-1]]:
                q.pop() 
            q.append(r)

            # Enforce policy of removing elements to the left of the window
            if l > q[0]:
                q.popleft()
            
            # We have a window of K, so add the largest element and increment l. Enforce fixed-window invariant
            if(r - l + 1) >= k:
                solution.append(nums[q[0]])
                l += 1

            # right pointer always moves
            r += 1
            print(f'Q: {[nums[i] for i in q]}, solution: {solution}')
        return solution
