class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = 0
        for r in range(k):
            curr_sum += nums[r]
        l = 0
        max_avg = curr_sum / k
        for r in range(k, len(nums)):
            curr_sum += nums[r]
            curr_sum -= nums[l]
            l += 1
            max_avg = max(max_avg, curr_sum / k)
        return max_avg