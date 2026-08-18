class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1
        
        heap = [-count for count in counts.values()]

        heapq.heapify(heap)
        queue = deque([])
        time = 0

        while heap or queue:
            time += 1
            if heap:
                count = heapq.heappop(heap) + 1
                if count:
                    add = n if n > 0 else 1
                    queue.append([count, time + add])
            else:
                time = queue[0][1]
            
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        
        return time
        