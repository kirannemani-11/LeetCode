class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        a = []
        for v in matrix:
            a.extend(v)
        a.sort()
        return a[k-1]