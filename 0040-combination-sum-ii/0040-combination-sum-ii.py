class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, comb, curr_sum):
            if curr_sum == target:
                res.append(comb[:])
                return
            if curr_sum > target or i >= len(candidates):
                return
            comb.append(candidates[i])
            dfs(i + 1, comb, curr_sum + candidates[i])
            comb.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, comb, curr_sum)
            
        dfs(0, [], 0)
        return res