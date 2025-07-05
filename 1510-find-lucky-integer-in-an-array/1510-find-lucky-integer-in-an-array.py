class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = [0] * 501
        for v in arr:
            count[v] += 1
        c = -1
        for i in range(1,len(count)-1):
            if i == count[i]:
                c = max(c, count[i])
        return c