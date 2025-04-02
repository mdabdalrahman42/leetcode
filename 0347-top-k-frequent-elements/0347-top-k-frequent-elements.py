class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1
        heap = [[-count[i], i] for i in count]
        heapq.heapify(heap)
        result = []
        while k > 0:
            _, i = heapq.heappop(heap)
            k -= 1
            result.append(i)
        return result