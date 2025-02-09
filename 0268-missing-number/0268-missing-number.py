class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # return sum([i for i in range(len(nums) + 1)]) - sum(nums)
        xor_nums = 0
        for i in nums:
            xor_nums ^= i
        xor_range = 0
        for i in range(len(nums) + 1):
            xor_range ^= i
        return xor_nums ^ xor_range