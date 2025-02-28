class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        def dfs(i):
            if i == len(s):
                return 1
            if i in dp:
                return dp[i]
            if s[i] == "0":
                dp[i] = 0
                return 0
            res = dfs(i + 1)
            if i + 1 < len(s) and int(s[i] + s[i + 1]) in range(10, 27):
                res += dfs(i + 2)
            dp[i] = res
            return dp[i]
        return dfs(0)