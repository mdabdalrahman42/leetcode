class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        part = []
        def ispali(i, j):
            l, r = i, j
            while l < r:
                if not s[l] == s[r]:
                    return False
                l += 1
                r -= 1
            return True
        def dfs(i):
            if i >= len(s):
                output.append(part[:])
                return
            for j in range(i, len(s)):
                if ispali(i, j):
                    part.append(s[i: j + 1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return output