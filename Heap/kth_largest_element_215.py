# Fact 1: Looking for k-th largest element in sorted order

# Observation 1: Can maintain a min-heap of size k to get the answer

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for i in nums[k:]:
            if i > min_heap[0]:
                heapq.heappushpop(min_heap, i)
        
        return min_heap[0]
