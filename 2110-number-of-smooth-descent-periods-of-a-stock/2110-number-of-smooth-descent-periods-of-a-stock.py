class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        curr = 1
        ans = 1
        for i in range(1, len(prices)):
            if prices[i-1] == prices[i] + 1:
                curr += 1
            else:
                curr = 1
            ans += curr
        return ans