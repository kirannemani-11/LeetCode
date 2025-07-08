class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i,v in enumerate(nums):
            if target - v in index.keys():
                return [index[target-v],i]
            else:
                index[v] = i