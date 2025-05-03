"""
Car has "capacity" empty seats. Cannot drive west.
- Only positive directionality.

trips[i] = [num_passengers, from, to] locations are given as the kilometer count due east FROM CAR'S INITIAL POSITION.

Return True if possible to complete the trip, false otherwise.

Some facts:
1. We will always have at least one trip
2. We will never be moving more than 1000.

Observation 1: Our problem invariant is that current_passengers must be less than capacity at all times. If ever violated, we return true.
Observation 2: If we sort trips by starting position, we may be able to aggregate the number of people in the car at each position, while monitoring the invariant.

There is literally no need to do all of the bookkeeping from the previous solution. We can track that effect using an aggregate sum variable. Additionally, what does each position of the prefix sum array represent? Keeping track of the nubmer of passengers at each position has a lot of book keeping involved, but keeping track of the change in the number of passengers, is much more simple and requires far less bookkeeping. 

"""

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        num_positions = max([trip[2] for trip in trips])
        capacity_at_each_position = [0] * (num_positions + 1)
        for cap, start, end in trips:
            capacity_at_each_position[start] += cap
            capacity_at_each_position[end] -= cap
        curr_passengers = 0
        for cap in capacity_at_each_position:
            curr_passengers += cap
            if curr_passengers > capacity:
                return False
        return True
