class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        right = 1
        prev = nums[0]
        while right < len(nums):
            if nums[right] > prev:
                nums[left] = nums[right]
                prev = nums[right]
                left += 1
            right += 1
        return left 