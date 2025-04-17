# Fact 1: For an array of numbers, return the K most frequent elements in it.
# Fact 2: Guaranteed that the answer is unique.

# Observation 1: Sort/Heap likely helps here. 
# Observation 2: The follow-up constraint implies that O(n log n) is not ideal. Perhaps a linear solution?
# Observation 3: We will need to generate a count of characters here to work with.
# Observation 4: The frequency of a character cannot exceed the length of the array itself, so we can create a "bucket" of len(nums) + 1 (because 0-index, item can occur len(nums) + 1 times)
# Observation 5: Map the frequency of a character to a list of characters with that frequency. 
# Observation 6: Can iterate backwards to get counts that monotonically decrease. 
# Observation 7: This is called "bucket sort." I did not come up with this on my own. Lol

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(0, len(nums) + 1)]

        for n,c in count.items():
            freq[c].append(n)
        
        sol = []

        i = len(freq) - 1
        while i >= 0 and len(sol) < k:
            if len(freq[i]) > 0:
                for j in freq[i]:
                    if(len(sol) == k):
                        break
                    sol.append(j)
            i -= 1
        return sol


class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = Counter(nums)
#         arr = []
#         for key, v in count.items():
#             arr.append((-v, key))
#         heapq.heapify(arr)
#         print(arr)
#         sol = []
#         while k > 0:
#             print(k)
#             freq, val = heapq.heappop(arr)
#             sol.append(val)
#             k -= 1
#         return sol
