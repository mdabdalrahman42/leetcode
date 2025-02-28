class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = set([0])
        for i in nums[-1::-1]:
            new_dp = set()
            for n in dp:
                new_dp.add(n + i)
                new_dp.add(n)
            dp = new_dp
        return True if target in dp else False