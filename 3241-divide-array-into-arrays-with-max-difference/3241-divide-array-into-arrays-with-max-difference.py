class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        a = []
        for i in range(0, len(nums) ,3):
            g = nums[i:i+3]
            if g[2] - g[0] > k:
                return []
            else:
                a.append(g[:])
        return a