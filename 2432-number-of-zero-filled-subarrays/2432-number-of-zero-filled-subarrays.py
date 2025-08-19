class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        m = 0
        c = 0
        for v in nums:
            if v == 0:
                c += 1
            else:
                m += ((c) * (c+1))//2
                c = 0
        if c>0:
            m += ((c) * (c+1))//2
        return m