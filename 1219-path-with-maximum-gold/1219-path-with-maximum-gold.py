class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        d = [(0,1), (0,-1), (1,0), (-1,0)]
        m = len(grid)
        n = len(grid[0])
        g = 0
        def backtrack(visited, i, j):
            gold = grid[i][j]
            best = 0
            for r,c in d:
                nr,nc = i+r, j+c
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 0 and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    best = max(best, backtrack(visited, nr, nc))
                    visited.remove((nr,nc))
            return gold + best
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    visited = {(i,j)}
                    g = max(g, backtrack(visited, i , j))
        return g