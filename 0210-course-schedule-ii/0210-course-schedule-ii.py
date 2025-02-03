class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(course):
            if course in visited:
                return False
            if adj_list[course] == []:
                if course not in order:
                    order.append(course)
                return True
            visited.append(course)
            for i in adj_list[course]:
                if not dfs(i):
                    return False
            visited.remove(course)
            adj_list[course] = []
            if course not in order:
                order.append(course)
            return True
        
        adj_list = {i:[] for i in range(numCourses)}
        for i in prerequisites:
            adj_list[i[0]].append(i[1])
        visited = []
        order = []
        for course in adj_list:
            if not dfs(course):
                return []
        return order