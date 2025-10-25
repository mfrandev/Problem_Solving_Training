class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        len_first, len_second = len(firstList), len(secondList)
        i, j = 0, 0
        ans = []
        while i < len_first and j < len_second:
            i1, i2 = firstList[i]
            j1, j2 = secondList[j]
            if i2 >= j1 and i1 <= j2: # we have overlap
                ans.append([max(i1, j1), min(i2, j2)])

            if i2 < j2:
                i+=1
            else:
                j+=1
        return ans