class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = set([0])
        for i in range(len(nums) - 1, -1, -1):
            new_dp = set()
            for s in dp:
                new_dp.add(s + nums[i])
                new_dp.add(s)
            dp = new_dp
        return True if target in dp else False