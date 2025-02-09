class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # return 2 * sum(set(nums)) - sum(nums)
        xor = 0
        for i in nums:
            xor ^= i
        return xor