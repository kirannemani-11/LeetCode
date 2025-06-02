from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        INF = m + n
        q = deque()
        dist = [[INF]*n for _ in range(m)]
        d = [(1,0), (-1,0), (0,1), (0,-1)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i,j))
        while q:
            i,j = q.popleft()
            for dr,dc in d:
                nr,nc = i + dr, j + dc
                if 0<=nr<m and 0 <= nc < n:
                    if dist[i][j] + 1 < dist[nr][nc]:
                        dist[nr][nc] = dist[i][j] + 1
                        q.append((nr,nc))
        return dist