class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = [None for i in range(len(nums))]
        l, r = 0, len(nums) - 1
        ind = len(nums) - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                output[ind] = nums[l] * nums[l]
                l += 1
            else:
                output[ind] = nums[r] * nums[r]
                r -= 1
            ind -= 1 
        return output