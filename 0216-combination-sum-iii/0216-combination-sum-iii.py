class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output = []
        comb = []
        def dfs(i, curr_sum):
            if curr_sum == n and len(comb) == k:
                output.append(comb[:])
                return
            if len(comb) > k or curr_sum > n or i > 9:
                return
            comb.append(i)
            dfs(i + 1, curr_sum + i)
            comb.pop()
            dfs(i + 1, curr_sum)
        dfs(1, 0)
        return output