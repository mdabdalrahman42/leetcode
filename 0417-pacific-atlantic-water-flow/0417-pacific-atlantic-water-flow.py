class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])
        output = []
        """
        def dfs(r, c, visited, height):
            visited.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for new_row, new_col in directions:
                new_row += r
                new_col += c
                if (new_row, new_col) not in visited and new_row in range(rows) and new_col in range(cols) and heights[new_row][new_col] >= height:
                    visited.add((new_row, new_col))
                    dfs(new_row, new_col, visited, heights[new_row][new_col])
        """
        def bfs(r, c, visited):
            visited.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            queue = deque([(r, c)])
            while queue:
                r, c = queue.popleft()
                height = heights[r][c]
                for new_row, new_col in directions:
                    new_row += r
                    new_col += c
                    if (new_row, new_col) not in visited and new_row in range(rows) and new_col in range(cols) and heights[new_row][new_col] >= height:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))

        for c in range(cols):
            #dfs(0, c, pacific, heights[0][c])
            #dfs(rows - 1, c, atlantic, heights[rows - 1][c])
            bfs(0, c, pacific)
            bfs(rows - 1, c, atlantic)
        for r in range(rows):
            #dfs(r, 0, pacific, heights[r][0])
            #dfs(r, cols - 1, atlantic, heights[r][cols - 1])
            bfs(r, 0, pacific)
            bfs(r, cols - 1, atlantic)
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    output.append([r, c])
        return output