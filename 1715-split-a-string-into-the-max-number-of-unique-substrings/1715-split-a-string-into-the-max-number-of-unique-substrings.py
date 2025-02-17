class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        visited = set()
        def dfs(i):
            if i >= len(s):
                return 0
            res = 0
            for j in range(i, len(s)):
                part = s[i:j + 1]
                if part not in visited:
                    visited.add(part)
                    res = max(res, 1 + dfs(j + 1))
                    visited.remove(part)
            return res
        return dfs(0)