class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(l, r):
            if l <= r:
                mid = l + (r - l) // 2
                if target == nums[mid]:
                    return mid
                if target > nums[mid]:
                    return bs(mid + 1, r)
                else:
                    return bs(l, mid - 1)
            return -1
        return bs(0, len(nums) - 1)