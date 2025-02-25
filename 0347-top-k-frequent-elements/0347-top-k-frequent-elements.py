class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i  not in count:
                count[i] = 0
            count[i] += 1
        bucket = [[] for i in range(len(nums))]
        for i in count:
            bucket[count[i] - 1].append(i)
        output = []
        for i in range(len(bucket) - 1, -1, -1):
            for j in range(len(bucket[i])):
                if len(bucket[i]) != 0:
                    output.append(bucket[i][j])
                    k -= 1
                if k == 0:
                    return output
            if k == 0:
                return output
