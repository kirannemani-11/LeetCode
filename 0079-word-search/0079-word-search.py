class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        d = [(0,1), (0,-1), (1,0), (-1,0)]
        def dfs(s):
            while s:
                i, j, k, visited = s.pop()
                if board[i][j] != word[k]:
                    continue
                if k == len(word) - 1:
                    return True
                visited[i][j] = True
                for dr, dc in d:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        if not visited[nr][nc]:
                            new_visited = [row[:] for row in visited]
                            s.append((nr, nc, k+1, new_visited))
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = [[False]*n for _ in range(m)]
                    s = [(i, j, 0, visited)]
                    if dfs(s):
                        return True
        return False