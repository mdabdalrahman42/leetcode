class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr_sum = 0
        min_len = float("inf")
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                curr_sum -= nums[l]
                min_len = min(min_len, r - l + 1)
                l += 1
        return 0 if min_len == float("inf") else min_len