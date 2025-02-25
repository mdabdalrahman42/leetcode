class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for i in s:
            if i not in count:
                count[i] = 0
            count[i] += 1
        heap = [[-count[i], i] for i in count]
        heapq.heapify(heap)
        output = ""
        for _ in range(len(count)):
            cnt, char = heapq.heappop(heap)
            output += char * (- cnt)
        return output