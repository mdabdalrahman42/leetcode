class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for i in tasks:
            if i not in count:
                count[i] = 0
            count[i] += 1
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)
        queue = deque([])
        time = 0
        while heap or queue:
            time += 1
            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt != 0:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue[0][0])
                queue.popleft()
        return time