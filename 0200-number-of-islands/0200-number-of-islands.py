class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        output = 0
        def bfs(r, c):
            queue = deque([(r, c)])
            while queue:
                r, c = queue.popleft()
                for new_row, new_col in directions:
                    new_row += r
                    new_col += c
                    if (new_row, new_col) not in visited and new_row in range(rows) and new_col in range(cols) and grid[new_row][new_col] == "1":
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    visited.add((r, c))
                    bfs(r, c)
                    output += 1
        return output