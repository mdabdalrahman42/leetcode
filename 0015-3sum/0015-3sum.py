class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):
            if not (i > 0 and nums[i] == nums[i - 1]):
                l, r = i + 1, len(nums) - 1
                while l < r:
                    curr_sum = nums[i] + nums[l] + nums[r]
                    if curr_sum < 0:
                        l += 1
                    elif curr_sum > 0:
                        r -= 1
                    else:
                        output.append([nums[i], nums[l], nums[r]])
                        while l + 1 < len(nums) and nums[l] == nums[l + 1]:
                            l += 1
                        l += 1
        return output