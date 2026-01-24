class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(arr):
            if len(arr) == 1:
                return arr[0]
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])
            return dp[-1]
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        le = dp(nums[:-1])
        fe = dp(nums[1:])
        return max(le,fe)