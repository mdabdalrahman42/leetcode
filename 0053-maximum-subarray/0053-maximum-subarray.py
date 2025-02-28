class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        output = float("-inf")
        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            output = max(output, curr_sum)
        return output