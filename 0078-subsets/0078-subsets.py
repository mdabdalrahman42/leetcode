class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for n in nums:
            for i in range(len(output)):
                output.append(output[i] + [n])
        return output
        