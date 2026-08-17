class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            s = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(heap, (-s, (x, y)))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = [point[1] for point in heap]
        return res
        