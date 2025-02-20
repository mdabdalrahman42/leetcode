class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        output = 0
        l = 0
        for r in range(len(nums)):
            product *= nums[r]
            while l<=r and product >= k:
                product = product // nums[l]
                l += 1
            output += r - l + 1
        return output