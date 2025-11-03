class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                return abs(nums[i])
            else:
                nums[abs(nums[i]) - 1] = - nums[abs(nums[i]) - 1]
        """
        """
        slow = fast = 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        """
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = l + (h - l) // 2
            count = sum([1 for n in nums if n <= mid])
            if count > mid:
                h = mid - 1
            else:
                l = mid + 1
        return l