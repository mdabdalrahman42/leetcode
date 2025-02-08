class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)
        for i in nums:
            if i - 1 not in nums:
                l = 1
                while i + l in nums:
                    l += 1
                longest = max(longest, l)
        return longest