class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(i, visited):
            if i == len(s):
                return 0
            res = 0
            for j in range(i, len(s)):
                if s[i:j + 1] not in visited:
                    visited.add(s[i:j + 1])
                    res = max(res, 1 + dfs(j + 1, visited))
                    visited.remove(s[i: j + 1])
            return res
        return dfs(0, set())