class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        input = set(nums)
        output = 0
        for i in input:
            if i - 1 not in input:
                l = 1
                while i + l in input:
                    l += 1
                output = max(output, l)
        return output