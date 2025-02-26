class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        for i in s:
            if i not in count:
                count[i] = 0
            count[i] += 1
        heap = [[-count[i], i] for i in count]
        heapq.heapify(heap)
        prev = None
        output = ""
        while heap:
            cnt, char = heapq.heappop(heap)
            output += char
            cnt += 1
            if prev:
                heapq.heappush(heap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        if prev:
            return ""
        return output