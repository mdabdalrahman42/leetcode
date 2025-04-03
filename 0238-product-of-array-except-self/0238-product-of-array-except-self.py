class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for i in range(1, len(nums)):
            left.append(left[i - 1] * nums[i - 1])
        right = [1]
        for i in range(len(nums) - 2, -1, -1):
            right.append(right[len(nums) - i - 2] * nums[i + 1])
        right.reverse()
        return [left[i] * right[i] for i in range(len(nums))]