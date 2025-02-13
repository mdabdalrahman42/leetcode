class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        def bfs(r, c, visited):
            visited.add((r, c))
            queue = deque([(r, c, heights[r][c])])
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while queue:
                r, c, height = queue.popleft()
                for new_row, new_col in directions:
                    new_row += r
                    new_col += c
                    if new_row in range(rows) and new_col in range(cols) and (new_row, new_col) not in visited and heights[new_row][new_col] >= height:
                        queue.append((new_row, new_col, heights[new_row][new_col]))
                        visited.add((new_row, new_col))
        for c in range(cols):
            bfs(0, c, pacific)
            bfs(rows - 1, c, atlantic)
        for r in range(rows):
            bfs(r, 0, pacific)
            bfs(r, cols - 1, atlantic)
        output = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    output.append([r, c])
        return output
        