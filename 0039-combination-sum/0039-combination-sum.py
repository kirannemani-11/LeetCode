class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        r = []
        candidates = sorted(candidates)
        def backtrack(arr, curr):
            if curr == target:
                c = sorted(arr)
                if c not in r:
                    r.append(arr[:])
            for v in candidates:
                if curr + v <= target:
                    arr.append(v)
                    backtrack(arr, curr+v)
                    arr.pop()
        for v in candidates:
            backtrack([v], v)
        return r