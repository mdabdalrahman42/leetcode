class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        if len(nums) == 1:
            return [nums[:]]
        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            output.extend(perms)
            nums.append(n)
        return output