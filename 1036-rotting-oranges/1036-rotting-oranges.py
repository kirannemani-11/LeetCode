from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        directions = [(1,0),  (-1,0), (0,1), (0,-1)]
        q = deque()
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        while q and fresh > 0:
            for _ in range(len(q)):
                i,j = q.popleft()
                for dr,dc in directions:
                    nr,nc = i + dr, j + dc
                    if 0<=nr<m and 0<=nc<n:
                        if grid[nr][nc] == 1:
                            fresh -= 1
                            grid[nr][nc] = 2
                            q.append((nr,nc))
            count += 1
        return count if fresh == 0 else -1