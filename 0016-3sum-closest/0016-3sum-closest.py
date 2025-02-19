class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float("inf")
        for i in range(len(nums)):
            if not (i > 0 and nums[i] == nums[i - 1]):
                l, r = i + 1, len(nums) - 1
                while l < r:
                    summ = nums[i] + nums[l] + nums[r]
                    if abs(target - summ) < abs(target - closest):
                        closest = summ
                    if summ == target:
                        return closest
                    elif summ > target:
                        r -= 1
                    else:
                        l += 1
        return closest