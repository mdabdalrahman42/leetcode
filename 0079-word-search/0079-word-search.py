class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def bfs(r, c, i):
            queue = deque([(r, c, i, {(r, c)})])
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            while queue:
                r, c, i, visited = queue.popleft()
                
                if i == len(word):  # Word found
                    return True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc  # Compute new position
                    
                    if (nr, nc) not in visited and 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == word[i]:
                        queue.append((nr, nc, i + 1, visited | {(nr, nc)}))
            
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if bfs(r, c, 1):
                        return True

        return False