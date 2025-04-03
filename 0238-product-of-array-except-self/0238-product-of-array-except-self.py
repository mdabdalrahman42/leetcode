class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        for i in range(len(nums) - 2, -1, -1):
            output.append(output[-1] * nums[i + 1])
        output.reverse()
        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
        return output