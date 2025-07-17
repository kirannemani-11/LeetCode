class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timetaken(k):
            hrs = 0
            for v in piles:
                hrs += (v+k-1) // k
            return hrs
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            hrs = timetaken(mid)
            if hrs <= h:
                right = mid
            else:
                left = mid + 1
        return left