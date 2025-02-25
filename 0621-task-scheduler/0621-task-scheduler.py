class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for i in tasks:
            if i not in count:
                count[i] = 0
            count[i] += 1
        heap = [-cnt for cnt in count.values()]
        time = 0
        heapq.heapify(heap)
        queue = deque([])
        while heap or queue:
            time += 1
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue[0][0])
                queue.popleft()
            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt:
                    queue.append([cnt, time + n + 1])
        return time