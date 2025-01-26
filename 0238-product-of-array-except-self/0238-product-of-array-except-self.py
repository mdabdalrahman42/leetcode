class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = [1]
        for i in range(1, len(nums)):
            right.append(nums[len(nums) - i] * right[i - 1])
        right.reverse()
        left = 1
        for i in range(len(nums)):
            right[i] *= left
            left = left * nums[i]
        return right
        # O(n) time and O(1) space (for space, right array is not considered as it is output)