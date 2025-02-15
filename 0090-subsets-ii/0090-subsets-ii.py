class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        def dfs(i, subset):
            if i >= len(nums):
                output.append(subset)
                return
            dfs(i + 1, subset + [nums[i]])
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, subset)
        dfs(0, [])
        return output