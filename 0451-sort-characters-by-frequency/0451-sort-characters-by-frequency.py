class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for i in s:
            if i not in count:
                count[i] = 0
            count[i] += 1
        bucket = [[] for _ in range(len(s))]
        for i in count:
            bucket[count[i] - 1].append(i)
        output = ""
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(bucket[i])):
                output += bucket[i][j] * (i + 1)
        return output