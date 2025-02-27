class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = {}
        def dfs(curr_sum, i):
            if (curr_sum, i) in dp:
                return dp[(curr_sum, i)]
            elif curr_sum == 0:
                dp[(curr_sum, i)] = True
                return True
            elif curr_sum < 0 or i == len(nums):
                return False
            if dfs(curr_sum - nums[i], i + 1):
                dp[(curr_sum, i)] = True
                return True
            elif dfs(curr_sum, i + 1):
                dp[(curr_sum, i)] = True
                return True
            dp[(curr_sum, i)] = False
            return dp[(curr_sum, i)]
        return dfs(target, 0)