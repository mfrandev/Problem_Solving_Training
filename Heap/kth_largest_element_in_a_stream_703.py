# Observation 1: No need to store the whole stream, only 'k' elements.
# Observation 2: Looking for a kth largest value, so we bias larger elements over smaller elements while maintaining a min heap
# Observation 3: Not necessary that the heap is initialized with at least k values, so need to make sure that subsequent adds when len(arr) < k are handled properly

class KthLargest:

    arr = []
    k = -1

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums[:k]
        heapq.heapify(self.arr)
        for i in range(k, len(nums)):
            if self.arr[0] < nums[i]:
                heapq.heappushpop(self.arr, nums[i])

    def add(self, val: int) -> int:
        if len(self.arr) < self.k:
            heapq.heappush(self.arr, val)
        elif self.arr[0] < val:
            heapq.heappushpop(self.arr, val)
        return self.arr[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
