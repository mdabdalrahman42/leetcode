class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct = set(nums)
        if len(nums) != len(distinct):
            return True
        else:
            return False