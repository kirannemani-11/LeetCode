class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minval = float('inf')
        for v in prices:
            minval = min(v, minval)
            maxProfit = max(maxProfit, v - minval)
        return maxProfit