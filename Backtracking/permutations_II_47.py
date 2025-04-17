class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result, perm = [], []
        freq = Counter(nums)

        def search():
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            
            for elem in freq:
                if freq[elem] > 0:
                    perm.append(elem)
                    freq[elem] -= 1

                    search()

                    perm.pop()
                    freq[elem] += 1

        search()
        return result
