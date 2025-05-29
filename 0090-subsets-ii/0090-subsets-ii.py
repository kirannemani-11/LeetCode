class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        r = set()
        nums = sorted(nums)
        def backtrack(curr, i):
            r.add(tuple(curr))
            for i in range(i, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i+1)
                curr.pop()
        backtrack([], 0)
        return list(r)