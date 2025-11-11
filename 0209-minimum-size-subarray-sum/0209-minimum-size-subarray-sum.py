class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = nums[i] + prefix[i-1]
        i = 0
        m = float('inf')
        curr = 0
        for j in range(0, len(nums)):
            if i:
                curr = prefix[j] - prefix[i-1]
            else:
                curr = prefix[j]
            while curr >= target:
                m = min(m, j-i+1)
                i += 1
                curr = prefix[j] - prefix[i-1]
        return 0 if m == float('inf') else m