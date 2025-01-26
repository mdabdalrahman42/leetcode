class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)
        nums = set(nums)
        output = []
        for i in range(1, l + 1):
            if i not in nums:
                output.append(i)
        return output