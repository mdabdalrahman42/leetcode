class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:        
        N = len(grid)
        dp = {}  # dictionary for memoization

        def solve(i, j, I, J):
            # invalid states
            if (i < 0 or i >= N or j < 0 or j >= N or
                I < 0 or I >= N or J < 0 or J >= N or
                grid[i][j] == -1 or grid[I][J] == -1):
                return -math.inf
            
            # if already computed
            if (i, j, I, J) in dp:
                return dp[(i, j, I, J)]
            
            # both reached bottom-right
            if i == N-1 and j == N-1 and I == N-1 and J == N-1:
                return grid[i][j]

            # collect cherries (avoid double counting if same cell)
            cherries = grid[i][j]
            if (i, j) != (I, J):
                cherries += grid[I][J]

            # 4 possible move combinations
            best = max(
                solve(i+1, j, I+1, J),   # both down
                solve(i, j+1, I, J+1),   # both right
                solve(i+1, j, I, J+1),   # 1 down, 2 right
                solve(i, j+1, I+1, J)    # 1 right, 2 down
            )

            dp[(i, j, I, J)] = cherries + best
            return dp[(i, j, I, J)]

        return max(0, solve(0, 0, 0, 0))