class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        pal = []
        def ispal(i, j):
            l, r = i, j
            while l < r:
                if not s[l] == s[r]:
                    return False
                l += 1
                r -= 1
            return True
        def dfs(i):
            if i >= len(s):
                res.append(pal.copy())
                return
            for j in range(i, len(s)):
                if ispal(i, j):
                    pal.append(s[i:j + 1])
                    dfs(j + 1)
                    pal.pop()
        dfs(0)
        return res