class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        dic = {i:0 for i in nums}
        for i in nums:
            dic[i] += 1
        def dfs():
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            for i in dic:
                if dic[i] > 0:
                    perm.append(i)
                    dic[i] -= 1
                    dfs()
                    dic[i] += 1
                    perm.pop()
        dfs()
        return result