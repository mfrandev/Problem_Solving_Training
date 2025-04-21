class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        
        result = []
        visiting = set()
        visited = set()

        def dfs(course) -> bool:
            if course in visiting:
                return False
            if course in visited:
                return True
            for prereq in adj_list[course]:
                visiting.add(course)
                if not dfs(prereq):
                    return False
                visiting.remove(course)
            result.append(course)
            visited.add(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
            visited.add(i)

        return result