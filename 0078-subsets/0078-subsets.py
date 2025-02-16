class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        output = []
        subset = []
        def dfs(i):
            if i == len(nums):
                output.append(subset[:])
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return output
        """
        output = [[]]
        for i in nums:
            for j in range(len(output)):
                output.append(output[j] + [i])
        return output