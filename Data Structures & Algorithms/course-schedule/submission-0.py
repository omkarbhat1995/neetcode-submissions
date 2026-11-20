class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj: List[List[int]] = [[] for _ in range(numCourses)]
        indegree: List[int] = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        # Start with all courses that have no prerequisites (in-degree of 0)
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        completed_courses = 0

        while queue:
            curr = queue.popleft()
            completed_courses += 1

            # Decrement the in-degree of all courses dependent on the completed course
            for dependent in adj[curr]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    queue.append(dependent)

        # If all courses were completed, the graph has no cycles
        return completed_courses == numCourses