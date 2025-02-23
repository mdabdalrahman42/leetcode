class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float("-inf")
        curr_sum = 0
        for i in range(k):
            curr_sum += nums[i]
        max_avg = max(max_avg, curr_sum / k)
        for i in range(k, len(nums)):
            curr_sum = curr_sum + nums[i] - nums[i - k]
            max_avg = max(max_avg, curr_sum / k)
        return max_avg