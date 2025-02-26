class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        curr_sum = 0
        for i in nums:
            curr_sum += i
            self.prefix.append(curr_sum)

    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefix[right]
        left_sum = self.prefix[left - 1] if left - 1 >= 0 else 0
        return right_sum - left_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)