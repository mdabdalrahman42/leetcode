class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        comb = []
        def dfs(i, curr_sum):
            if curr_sum == target:
                output.append(comb[:])
                return
            if curr_sum > target or i >= len(candidates):
                return
            comb.append(candidates[i])
            dfs(i, curr_sum + candidates[i])
            comb.pop()
            dfs(i + 1, curr_sum)
        dfs(0, 0)
        return output