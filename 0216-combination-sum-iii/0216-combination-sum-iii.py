class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(i, comb, curr_sum):
            if len(comb) == k and curr_sum == n:
                res.append(comb[:])
                return
            if len(comb) > k or curr_sum > n or i > 9:
                return
            comb.append(i)
            dfs(i + 1, comb, curr_sum + i)
            comb.pop()
            dfs(i + 1, comb, curr_sum)
        dfs(1, [], 0)
        return res