class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = {i:[] for i in range(numCourses)}
        output = []
        for crs, prereq in prerequisites:
            dic[crs].append(prereq)
        visited = set()
        def dfs(course):
            if course in output:
                return True
            if dic[course] == []:
                output.append(course)
                return True
            if course in visited:
                return False
            visited.add(course)
            for prereq in dic[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            dic[course] = []
            output.append(course)
            return True
        for i in dic:
            if not dfs(i):
                return []
        return output