"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
- Input is an array of [x, y] coordinates
- All points [x, y] in the input are unique

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
- abs(x1 - x2) + abs(y1 - y2)

Return the edge weight sum of a MST on this graph.

"""

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's algorithm needs some state:
        # 1. track solution
        solution = 0
        # 2. min-heap. Heapq orders lexicographically, so cost must come first since we want to minimize cost. [(cost, index_of_arbitrarily_selected_starting_vertex)]
        heap = [(0,0)]
        # 3. We need to maintain state on the shortest distance between two points encountered thus far. Otherwise, we wouldn't know when to update our MST
        min_distance_cache = {0: 0}
        num_points = len(points)

        # 4. "Visited" tracker, so as to avoid running into cycles
        visited = [False] * num_points

        while heap:
            cost, starting_vertex_index = heapq.heappop(heap)
            if visited[starting_vertex_index]:
                continue
            # Remember, this only works because we are greedily taking the edges that "must" be part of the solution because of the min-heap invariant
            solution += cost
            visited[starting_vertex_index] = True

            # Now, we need to visit every point from the current point to see if we can find optimal path
            for destination_vertex_index in range(num_points):

                # If optimal path already found, skip this node
                if visited[destination_vertex_index]:
                    continue
                
                # Get manhattan distance
                dist = abs(points[starting_vertex_index][1] - points[destination_vertex_index][1]) + abs(points[starting_vertex_index][0] - points[destination_vertex_index][0])

                # If our manhattan distance is the optimal solution, cache it, and add the distance to the heap
                if dist < min_distance_cache.get(destination_vertex_index, float("inf")):
                    min_distance_cache[destination_vertex_index] = dist
                    heapq.heappush(heap, (dist, destination_vertex_index))
        return solution
