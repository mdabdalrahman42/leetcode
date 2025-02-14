class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = {i:[] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            dic[crs].append(prereq)
        visited = set()
        output = []

        def dfs(course):
            if dic[course] == []:
                if course not in output:
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
            if course not in output:
                output.append(course)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output