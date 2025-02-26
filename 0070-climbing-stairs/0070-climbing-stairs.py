class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {n:1}
        def dfs(curr_sum):
            if curr_sum in dp:
                return dp[curr_sum]
            if curr_sum > n:
                return 0
            dp[curr_sum] = dfs(curr_sum + 1) + dfs(curr_sum + 2)
            return dp[curr_sum]
        dfs(0)
        return dp[0]