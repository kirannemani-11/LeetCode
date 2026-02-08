class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        b = 0
        for i in range(len(s)):
            if s[i] == 'b':
                b+=1
                dp[i+1] = dp[i]
            else:
                dp[i+1] = min(dp[i]+1, b)
        return dp[-1]