class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for i in range(1, len(nums)):
            left.append(left[i - 1] * nums[i - 1])
        left.reverse()
        nums.reverse()
        right = 1
        for i in range(len(nums)):
            left[i] *= right
            right *= nums[i]
        left.reverse()
        return left