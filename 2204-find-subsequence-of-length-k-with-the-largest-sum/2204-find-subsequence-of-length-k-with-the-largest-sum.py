import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        pq = []
        for i,v in enumerate(nums):
            heapq.heappush(pq, (v,i))
            if len(pq) > k:
                heapq.heappop(pq)
        top = sorted(pq, key = lambda x:x[1])
        return [val for val,i in top]