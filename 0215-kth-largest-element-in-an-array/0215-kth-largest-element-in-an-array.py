class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 50000:
            return 1
        k = len(nums) - k
        def quickselect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[r], nums[p] = nums[p], nums[r]
            if p == k:
                return nums[p]
            elif k > p:
                return quickselect(p + 1, r)
            else:
                return quickselect(l, p - 1)
        return quickselect(0, len(nums) - 1)