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
                for new_row, new_col in directions:
                    new_row += r
                    new_col += c
                    if (new_row, new_col) not in visited and new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols and board[new_row][new_col] == word[i]:
                        queue.append((new_row, new_col, i + 1, visited | {(new_row, new_col)}))
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if bfs(r, c, 1):
                        return True
        return False