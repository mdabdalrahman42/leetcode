class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        # Step 2: make a max-heap (store as negative for max behavior)
        heap = [-cnt for cnt in freq.values()]
        heapq.heapify(heap)
        
        # Step 3: pair elements
        while len(heap) >= 2:
            x = -heapq.heappop(heap)  # most frequent
            y = -heapq.heappop(heap)  # second most frequent
            
            # remove one occurrence each
            x -= 1
            y -= 1
            
            if x > 0:
                heapq.heappush(heap, -x)
            if y > 0:
                heapq.heappush(heap, -y)
        
        # Step 4: what's left
        return -heap[0] if heap else 0