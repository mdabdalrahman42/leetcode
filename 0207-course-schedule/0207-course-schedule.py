class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {i:[] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            dic[crs].append(prereq)
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
            visited.remove(course)
            dic[course] = []
            return True
        for i in dic:
            if not dfs(i):
                return False
        return True