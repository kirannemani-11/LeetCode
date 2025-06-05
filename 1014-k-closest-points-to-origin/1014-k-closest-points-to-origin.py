import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def findd(x1,y1):
            x2,y2 = 0, 0
            d = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
            return d
        pq = []
        heapq.heapify(pq)
        for x,y in points:
            d = findd(x,y)
            heapq.heappush(pq,(d,x,y))
        ans = []
        while pq and k>=1:
            v,x,y = heapq.heappop(pq)
            k-=1
            ans.append([x,y])
        return ans 