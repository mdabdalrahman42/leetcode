class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        output = 0

        """
        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))
            while queue:
                r, c = queue.pop()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for row_new, col_new in directions:
                     row_new += r
                     col_new += c
                     if row_new in range(rows) and col_new in range(cols) and (row_new, col_new) not in visited and grid[row_new][col_new] == "1":
                        queue.append((row_new, col_new))
                        visited.add((row_new, col_new))
        """

        def dfs(r, c):
            visited.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for row_new, col_new in directions:
                row_new += r
                col_new += c
                if row_new in range(rows) and col_new in range(cols) and (row_new, col_new) not in visited and grid[row_new][col_new] == "1":
                    dfs(row_new, col_new)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    output += 1
        return output