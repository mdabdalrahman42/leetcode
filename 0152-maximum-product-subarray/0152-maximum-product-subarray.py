class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = max(nums)
        curr_max, curr_min = 1, 1
        for n in nums:
            if n == 0:
                curr_max, curr_min = 1, 1
                continue
            temp = curr_max
            curr_max = max(curr_max * n, curr_min * n, n)
            curr_min = min(temp * n, curr_min * n, n)
            output = max(output, curr_max)
        return output