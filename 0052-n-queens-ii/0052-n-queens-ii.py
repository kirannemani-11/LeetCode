class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        def backtrack(visited):
            nonlocal count
            i = len(visited)
            if i == n:
                count += 1
                return
            for j in range(n):
                s = i + j
                d = i - j
                valid = True
                for r,c in visited:
                    if c == j:
                        valid = False
                        break
                    elif s == r+c or d == r-c:
                        valid = False
                        break
                if valid:
                    visited.append((i,j))
                    backtrack(visited)
                    visited.pop()
        backtrack([])
        return count