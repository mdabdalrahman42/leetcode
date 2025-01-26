class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Converting list to set takes O(n) complexity
        distinct = set(nums)
        if len(nums) != len(distinct):
            return True
        else:
            return False