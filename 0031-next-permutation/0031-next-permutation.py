class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        if pivot != -1:
            j = -1
            for i in range(len(nums)-1, 0, -1):
                if nums[i] > nums[pivot]:
                    j = i
                    break
            nums[pivot], nums[j] = nums[j], nums[pivot]
            nums[pivot+1:] = reversed(nums[pivot+1:])
        else:
            nums.sort()