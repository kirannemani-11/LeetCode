class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        freq = set()
        left = 0
        right = 0
        maxvalue = 0
        curr = 0
        for right in range(len(nums)):
            if nums[right] not in freq:
                freq.add(nums[right])
                curr += nums[right]
                maxvalue = max(maxvalue, curr)
            else:
                curr += nums[right]
                while nums[right] in freq:
                    freq.remove(nums[left])
                    curr -= nums[left]
                    left += 1
                freq.add(nums[right])
        return maxvalue