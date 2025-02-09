class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        output = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = - nums[abs(nums[i]) - 1]
        for i in range(len(nums)):
            if nums[i] > 0:
                output.append(i + 1)
        return output
        """
        n = len(nums)
        nums = set(nums)
        return [i for i in range(1, n + 1) if i not in nums]
