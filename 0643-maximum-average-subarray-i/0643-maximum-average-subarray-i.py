class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        curr_sum = 0
        for r in range(k):
            curr_sum += nums[r]
        max_avg = curr_sum / k
        for r in range(k, len(nums)):
            curr_sum -= nums[l]
            l += 1
            curr_sum += nums[r]
            max_avg = max(max_avg, curr_sum / k)
        return max_avg