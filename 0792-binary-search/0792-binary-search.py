class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(l, r):
            if l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    return bs(l, mid - 1)
                if nums[mid] < target:
                    return bs(mid + 1, r)
            return -1
        return bs(0, len(nums) - 1)