import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = []
        for r in matrix:
            for v in r:
                pq.append(v)
        heapq.heapify(pq)
        while k > 1:
            heapq.heappop(pq)
            k-=1
        return heapq.heappop(pq)