class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(course):
            if course in visited:
                return False
            if adj_list[course] == []:
                return True
            visited.append(course)
            for i in adj_list[course]:
                if not dfs(i):
                    return False
            visited.remove(course)
            adj_list[course] = []
            return True
        
        adj_list = {i:[] for i in range(numCourses)}
        for i in prerequisites:
            adj_list[i[0]].append(i[1])
        visited = []
        for course in adj_list:
            if not dfs(course):
                return False
        return True

        
