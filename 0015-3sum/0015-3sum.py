class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)):
            if not (i > 0 and nums[i] == nums[i - 1]):
                l, r = i + 1, len(nums) - 1
                while l < r:
                    summ = nums[i] + nums[l] + nums[r]
                    if summ > 0:
                        r -= 1
                    elif summ < 0:
                        l += 1
                    else:
                        output.append([nums[i], nums[l], nums[r]])
                        while l + 1 < r and nums[l] == nums[l + 1]:
                            l += 1
                        l += 1
        return output
                