class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min, curr_max = 1, 1
        output = max(nums)
        for n in nums:
            if n == 0:
                curr_min, curr_max = 1, 1
                continue
            temp = curr_max
            curr_max = max(n * curr_max, n * curr_min, n)
            curr_min = min(n * temp, n * curr_min, n)
            output = max(output, curr_max)
        return output