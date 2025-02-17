class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        comb = []
        def dfs(i):
            if len(comb) == k:
                output.append(comb[:])
                return
            for j in range(i, n + 1):
                comb.append(j)
                dfs(j + 1)
                comb.pop()
        dfs(1)
        return output