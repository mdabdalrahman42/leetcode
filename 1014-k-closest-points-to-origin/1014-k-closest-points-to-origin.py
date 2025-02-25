class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [[points[i][0] * points[i][0] + points[i][1] * points[i][1], i] for i in range(len(points))]
        heapq.heapify(heap)
        output = []
        while k > 0:
            _, i = heapq.heappop(heap)
            output.append(points[i])
            k -= 1
        return output