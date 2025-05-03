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

"""

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if len(trips) == 1:
            return trips[0][0] <= capacity
        trips.sort(key = lambda trip: trip[1])
        num_positions = max([trip[2] for trip in trips])
        capacity_at_each_position = [0] * num_positions
        capacity_at_each_position[0] = trips[0][0] if trips[0][1] != trips[0][2] else 0
        if capacity_at_each_position[0] > capacity:
            return False
        tracker = {}
        if capacity_at_each_position[0] != 0:
            tracker[trips[0][2]] = trips[0][0]
        trips_iter = 1
        for i in range(1, num_positions):
            cap, start, end = trips[trips_iter] if trips_iter < len(trips) else [-1, -1, -1]
            pickup = 0
            while start == i:
                pickup += cap
                if end in tracker:
                    tracker[end] += cap
                else:
                    tracker[end] = cap
                trips_iter += 1
                cap, start, end = trips[trips_iter] if trips_iter < len(trips) else [-1, -1, -1]
            dropoff = tracker.get(i, 0)
            cap_at_i = capacity_at_each_position[i - 1] + pickup - dropoff
            if cap_at_i > capacity:
                return False
            capacity_at_each_position[i] = cap_at_i
        return True
        
            
