class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        m = abs(nums[-1] - nums[0])
        for i in range(len(nums)-1, 0, -1):
            m = max(m , abs(nums[i-1] - nums[i]))
        return m