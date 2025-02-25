class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i in points:
            dist.append(i[0] * i[0] + i[1] * i[1])
        heap = [[-dist[i], i] for i in range(len(dist))]
        heapq.heapify(heap)
        for _ in range(len(dist) - k):
            heapq.heappop(heap)
        output = []
        for i in heap:
            output.append(points[i[1]])
        return output