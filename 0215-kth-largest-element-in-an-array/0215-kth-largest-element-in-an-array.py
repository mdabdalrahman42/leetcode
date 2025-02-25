class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-i for i in nums]
        heapq.heapify(heap)
        while True:
            n = - heapq.heappop(heap)
            k -= 1
            if k == 0:
                return n