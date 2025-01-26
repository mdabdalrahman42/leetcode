class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p1 = 0
        for p2 in range(p1, len(nums)):
            if nums[p2] != 0:
                nums[p1] = nums[p2]
                p1 += 1
        for i in range(p1, len(nums)):
            nums[i] = 0