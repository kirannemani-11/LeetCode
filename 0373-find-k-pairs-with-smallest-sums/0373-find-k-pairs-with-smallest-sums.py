class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = []
        for i in range(min(len(nums1),k)):
            heapq.heappush(pq, (nums1[i]+nums2[0], i, 0))
        ans = []
        while pq and len(ans) < k:
            v,i,j = heapq.heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if j+1 < len(nums2):
                n = nums1[i] + nums2[j+1]
                heapq.heappush(pq, (n,i,j+1))
        return ans