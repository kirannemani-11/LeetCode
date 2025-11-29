import math
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return math.ceil(sum(nums) % k)