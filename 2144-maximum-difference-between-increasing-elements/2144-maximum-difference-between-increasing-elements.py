class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mi = nums[0]
        m = -1
        for i in range(1, len(nums)):
            if nums[i] > mi:
                m = max(m, nums[i] - mi)
            else:
                mi = nums[i]
        return m