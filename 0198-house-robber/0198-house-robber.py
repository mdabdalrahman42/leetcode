class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(curr_sum, i):
            if (curr_sum, i) in dp:
                return dp[(curr_sum, i)]
            if i >= len(nums):
                return curr_sum
            dp[(curr_sum, i)] = max(dfs(curr_sum + nums[i], i + 2), dfs(curr_sum, i + 1))
            return dp[(curr_sum, i)]
        return dfs(0, 0)