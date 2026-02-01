class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return sum(nums)
        l1 = float('inf')
        l2 = float('inf')
        for i in range(1, len(nums)):
            if nums[i] < l1:
                l2 = l1
                l1 = nums[i]
            elif nums[i] < l2:
                l2 = nums[i]

        return nums[0] + l1 + l2