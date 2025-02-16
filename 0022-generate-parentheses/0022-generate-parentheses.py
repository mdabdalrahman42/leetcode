class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        string = []
        def dfs(open, close):
            if open == close == n:
                res.append("".join(string.copy()))
                return
            if open > n or close > open:
                return
            if open < n:
                string.append("(")
                dfs(open + 1, close)
                string.pop()
            if close < open:
                string.append(")")
                dfs(open, close + 1)
                string.pop()
        dfs(0, 0)
        return res