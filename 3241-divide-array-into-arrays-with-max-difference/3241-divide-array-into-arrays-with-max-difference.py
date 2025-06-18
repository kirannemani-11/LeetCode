class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        a = []
        for i in range(0, len(nums) ,3):
            g = nums[i:i+3]
            if len(g) < 3 or g[2] - g[0] > k:
                return []
            else:
                a.append(g[:])
        return a