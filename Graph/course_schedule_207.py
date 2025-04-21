"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
- Prerequisites is a list of tuples, [x, y], where y must be satisfied in order to take x.
- This looks like an adjacency list, where x and y are connected, and y flows to x
- Know we can use BFS, DFS to easily traverse a graph
- Probably want to use DFS here because it fully explore a path before moving to the next
- Need to track which courses we've taken already

Return true if you can finish all courses. Otherwise, return false.
- Looking for "can_take_all_courses," which is a boolean

Ex 1: [[1, 0]]: "Must take course 0, in order to take course 1."
- Start at 0. See there are no conflicts, so we can take course 0, then course 1.

Ex 2: [[1, 0], [0, 1]]: "In order to take course 1, must first take course 0. In order to take course 0, must first take course 1." This creates a cycle.

Problem reduces to: "Is there a cycle in the graph?"

1. Create an adjacency list of the input.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        active_courses = set()

        def can_take_all_courses_from(course: int) -> bool:
            if course in active_courses:
                return False
            if  len(adj_list[course]) == 0:
                return True
            active_courses.add(course)
            for i in range(len(adj_list[course]) - 1, -1, -1):
                if not can_take_all_courses_from(adj_list[course][i]):
                    return False
                adj_list[course].pop()
            active_courses.remove(course)
            return True
        
        for i in range(numCourses):
            if not can_take_all_courses_from(i):
                return False
        return True