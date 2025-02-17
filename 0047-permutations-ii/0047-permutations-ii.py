class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        dic = {i:0 for i in nums}
        for i in nums:
            dic[i] += 1
        output = []
        perm = []
        def dfs():
            if len(perm) == len(nums):
                output.append(perm[:])
                return
            for n in dic:
                if dic[n] > 0:
                    dic[n] -= 1
                    perm.append(n)
                    dfs()
                    perm.pop()
                    dic[n] += 1
        dfs()
        return output