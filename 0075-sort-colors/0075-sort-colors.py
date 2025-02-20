class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        l, r = 0, len(nums) - 1
        ind = 0
        while ind <= r:
            if nums[ind] == 0:
                swap(l, ind)
                l += 1
            elif nums[ind] == 2:
                swap(r, ind)
                r -= 1
                ind -= 1
            ind += 1