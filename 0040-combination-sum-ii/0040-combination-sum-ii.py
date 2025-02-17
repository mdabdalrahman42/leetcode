class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        comb = []
        def dfs(i, curr_sum):
            if curr_sum == target:
                output.append(comb[:])
                return
            if i >= len(candidates) or curr_sum > target:
                return
            comb.append(candidates[i])
            dfs(i + 1, curr_sum + candidates[i])
            comb.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr_sum)
        candidates.sort()
        dfs(0, 0)
        return output