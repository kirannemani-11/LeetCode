from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]
        islands = 0
        d = [(1,0), (-1,0), (0,1), (0,-1)]
        def bfs(q):
            while q:
                i,j = q.popleft()
                visited[i][j] = True
                grid[i][j] = '0'
                for dr, dc in d:
                    nr, nc = i + dr, j + dc
                    if 0<=nr<m and 0<=nc<n:
                        if grid[nr][nc] == '1':
                            q.append((nr,nc))
                            grid[nr][nc] = '0'
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    q = deque()
                    q.append((i,j))
                    islands += 1
                    bfs(q)
        return islands