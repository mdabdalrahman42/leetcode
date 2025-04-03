class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        for i in range(1, len(nums)):
            output.append(output[i - 1] * nums[i - 1])
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]
        return output