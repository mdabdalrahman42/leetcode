class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """ O(n) time and space
        left = [1]
        right = [1]
        for i in range(1, len(nums)):
            left.append(nums[i - 1] * left[i - 1])
        for i in range(len(nums)-2, -1, -1):
            right.append(nums[i + 1] * right[len(nums) - i - 2])
        right.reverse()
        return [left[i] * right[i] for i in range(len(nums))] """

        right = [1]
        for i in range(len(nums)-2, -1, -1):
            right.append(nums[i + 1] * right[len(nums) - i - 2])
        right.reverse()
        left = 1
        for i in range(0, len(nums)):
            right[i] = right[i] * left
            left *= nums[i]
        return right