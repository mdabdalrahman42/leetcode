class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float("inf")
        for i in range(len(nums)):
            if not (i > 0 and nums[i] == nums[i - 1]):
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    curr_sum = nums[i] + nums[l] + nums[r]
                    if abs(target - curr_sum) < abs(target - closest):
                        closest = curr_sum
                    if curr_sum > target:
                        r -= 1
                    elif curr_sum < target:
                        l += 1
                    else:
                        return target
        return closest