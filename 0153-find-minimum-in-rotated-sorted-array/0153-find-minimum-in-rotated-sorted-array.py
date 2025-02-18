class Solution:
    def findMin(self, nums: List[int]) -> int:
        output = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            output = min(output, nums[mid])
            if nums[l] <= nums[mid] and nums[r] >= nums[mid]:
                output = min(output, nums[l])
                break
            elif nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return output