class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def bfs(r, c, i):
            queue = deque([(r, c, i, {(r, c)})])
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while queue:
                r, c, i, visited = queue.popleft()
                if i == len(word):
                    return True
                for nr, nc in directions:
                    new_row = r + nr
                    new_col = c + nc
                    if (new_row, new_col) not in visited and 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] == word[i]:
                        queue.append((new_row, new_col, i + 1, visited | {(new_row, new_col)}))
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if bfs(r, c, 1):
                        return True
        return False