"""
N children, each child's rating is mapped to ratings[i], where ratings is guaranteed to be of length N.

Invariants: 
1. Each child needs at least one candy.
2. Children with ratings strictly higher than their neighbors get more candy.

We are returning the minimum number of candies we need to distribute to the children, since we really care about their health :)

Constraint 2 states that n will be no larger than 20,000, implying that we should be able to find an O(n) solution to this problem.
Constraint 3 states that all ratings will be non-negative.

Observation 1: The child with the lowest rating will get one candy.
Observation 2: The least amount of candy we can ever distribute is N pieces, which happens when all ratings are equal.
Observation 3: Observation 2 implies that higher local variance will increase the amount of candy distributed.
Observation 4: Not just the child with the lowest rating, but any child which is a local minima (n - 1 >= n <= n + 1) will receive one candy. 
Observation 5: A rating is either a local maxmia, local minima, or neither.

Case minima: We give one candy.
Case maxima: We give the current l-to-r candy count.
case neither: 

"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        map = [1] * n

        # print(f'ratings: {ratings}')

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                map[i] = map[i - 1] + 1
        
        # print(f'map left: {map}')

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and map[i] <= map[i + 1]:
                map[i] = map[i + 1] + 1 

        # print(f'map right: {map}')

        return sum(map)
        
