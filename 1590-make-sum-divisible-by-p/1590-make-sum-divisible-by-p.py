class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        s = sum(nums)
        total = s % p
        if total == 0:
            return 0
        else:
            curr = 0
            best = len(nums)
            fs = {0:-1}
            for i in range(len(nums)):
                curr = (curr + nums[i]) % p
                target = (curr - total) % p
                if target in fs:
                    best = min(best, i - fs[target])
                fs[curr] = i
        if best == len(nums):
            return -1
        return best