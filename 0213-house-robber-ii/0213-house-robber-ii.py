class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            rob1, rob2 = 0, 0
            for n in arr:
                temp = rob1
                rob1 = max(n + rob2, rob1)
                rob2 = temp
            return rob1
        return max(helper(nums[1:]), helper(nums[:-1]), nums[0])