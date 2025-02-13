class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = {i:[] for i in range(numCourses)}
        for v1, v2 in prerequisites:
            dic[v1].append(v2)
        visited = set()
        output = []

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
            dic[course] = []
            output.append(course)
            visited.remove(course)
            return True
                
        for course in range(numCourses):
            if not dfs(course):
                return []
        return output