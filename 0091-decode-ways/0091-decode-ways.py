class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i == len(s):
                dp[i] = 1
                return 1
            if s[i] == "0":
                dp[i] = 0
                return 0
            output = dfs(i + 1)
            if i + 1 < len(s) and int(s[i] + s[i + 1]) in range(10, 27):
                output += dfs(i + 2)
            dp[i] = output
            return output
        dfs(0)
        return dp[0]