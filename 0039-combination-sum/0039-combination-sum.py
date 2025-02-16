class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, comb, curr_sum):
            if curr_sum == target:
                res.append(comb[:])
                return
            if i >= len(candidates) or curr_sum > target:
                return
            comb.append(candidates[i])
            dfs(i, comb, curr_sum + candidates[i])
            comb.pop()
            dfs(i + 1, comb, curr_sum)
        dfs(0, [], 0)
        return res