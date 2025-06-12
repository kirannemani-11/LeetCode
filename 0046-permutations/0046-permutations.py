class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        r = []
        n = len(nums)
        def perm(curr):
            if len(curr) == n:
                r.append(curr[:])
            else:
                for v in nums:
                    if v not in curr:
                        curr.append(v)
                        perm(curr)
                        curr.pop()
        perm([])
        return r