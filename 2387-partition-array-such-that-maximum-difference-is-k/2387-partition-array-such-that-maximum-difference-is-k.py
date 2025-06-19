class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        c = 0
        mi = nums[0]
        for i in range(1,len(nums)):
            if nums[i] - mi > k:
                mi = nums[i]
                c+=1
        return c+1