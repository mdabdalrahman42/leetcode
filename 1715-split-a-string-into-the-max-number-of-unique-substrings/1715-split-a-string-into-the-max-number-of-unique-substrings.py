class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        visited = set()
        def dfs(i):
            if i == len(s):
                return 0
            res = 0
            for j in range(i, len(s)):
                sub = s[i:j + 1]
                if sub not in visited:
                    visited.add(sub)
                    res = max(res, 1 + dfs(j + 1))
                    visited.remove(sub)
            return res
        return dfs(0)