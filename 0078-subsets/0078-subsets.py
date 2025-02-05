class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for i in nums:
            for j in range(len(subsets)):
                subsets.append(subsets[j] + [i])
        return subsets