# 1. Sorted in ascending order, implies some sort of binary search or window ?
# 2. We need some way to say what the maximum number of fruits harvested at i position is after m moves

class Solution:
    def maxTotalFruits(self, fruits, startPos: int, k: int) -> int:
        left,agg,res=0,0,0
        for i in range(len(fruits)):
            agg+=fruits[i][1]
            while left<=i and min(
                abs(startPos-fruits[left][0])+fruits[i][0]-fruits[left][0],
                abs(fruits[i][0]-startPos)+fruits[i][0]-fruits[left][0]
            ) > k:
                agg-=fruits[left][1]
                left+=1
            res=max(agg,res)
        return res