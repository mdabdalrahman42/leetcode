class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = [0 for i in nums]
        i = len(nums) - 1
        l, r = 0, len(nums) - 1
        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                output[i] = nums[l] * nums[l]
                l += 1
            else:
                output[i] = nums[r] * nums[r]
                r -= 1
            i -= 1
        return output