class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cs = [0] * 3
        for v in nums:
            cs[v] += 1
        i = 0
        for j,v in enumerate(cs):
            for _ in range(v):
                nums[i] = j
                i += 1 