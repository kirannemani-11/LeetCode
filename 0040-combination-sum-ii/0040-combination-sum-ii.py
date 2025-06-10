class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        r = []
        def comb(curr, i):
            s = sum(curr)
            if s == target:
                r.append(curr[:])
            elif s > target:
                return 
            else:
                for k in range(i, len(candidates)):
                    if k > i and candidates[k] == candidates[k-1]:
                        continue
                    if s + candidates[k] > target:
                        break
                    curr.append(candidates[k])
                    comb(curr, k+1)
                    curr.pop()
        comb([], 0)
        return r