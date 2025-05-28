class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def sd(val):
            m = 0
            for v in nums:
                m += (v + val - 1) // val
            return m
        left = 1
        right = max(nums)
        ans = right
        while left <= right:
            mid = left + (right - left) // 2
            if sd(mid) <= threshold:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1 
        return ans