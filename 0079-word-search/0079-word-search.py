class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for new_row, new_col in directions:
                new_row += r
                new_col += c
                if (new_row, new_col) not in visited and new_row in range(rows) and new_col in range(cols) and board[new_row][new_col] == word[i]:
                    visited.add((new_row, new_col))
                    if dfs(new_row, new_col, i + 1):
                        return True
                    visited.remove((new_row, new_col))
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    visited.add((r, c))
                    if dfs(r, c, 1):
                        return True
                    visited.remove((r, c))
        return False