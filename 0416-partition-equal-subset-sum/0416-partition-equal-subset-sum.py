class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = {}
        def dfs(curr_sum, i):
            if curr_sum == 0:
                return True
            if curr_sum < 0 or i >= len(nums):
                return False
            if (curr_sum, i) in dp:
                return dp[(curr_sum, i)]
            if dfs(curr_sum - nums[i], i + 1):
                return True
            if dfs(curr_sum, i + 1):
                return True
            dp[(curr_sum, i)] = False
            return False
        return dfs(target, 0)