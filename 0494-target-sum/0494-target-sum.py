class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(curr_sum, i):
            if (curr_sum, i) in dp:
                return dp[(curr_sum, i)]
            if i == len(nums):
                if curr_sum == target:
                    dp[(curr_sum, i)] = 1
                    return 1
                else:
                    dp[(curr_sum, i)] = 0
                    return 0
            dp[(curr_sum, i)] = dfs(curr_sum + nums[i], i + 1) + dfs(curr_sum - nums[i], i + 1)
            return dp[(curr_sum, i)]
        return dfs(0, 0)
            