class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        ma = int(s)
        mi = float('inf')
        for val in s:
            v = int(val)
            if v < 9:
                ns = s.replace(val, '9')
                ma = int(ns)
                break
        for val in s:
            v = int(val)
            if v >= 1:
                ns = s.replace(val, '0')
                mi = int(ns)
                break
        print(ma)
        print(mi)
        return ma - mi