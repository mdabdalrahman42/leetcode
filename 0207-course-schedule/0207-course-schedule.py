class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {i:[] for i in range(numCourses)}
        for v1, v2 in prerequisites:
            dic[v1].append(v2)
        visited = set()

        def dfs(course):
            if dic[course] == []:
                return True
            if course in visited:
                return False
            visited.add(course)
            for prereq in dic[course]:
                if not dfs(prereq):
                    return False
            dic[course] = []
            visited.remove(course)
            return True
                
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True