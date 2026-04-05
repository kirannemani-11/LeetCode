class Solution:
    def judgeCircle(self, moves: str) -> bool:
        a,b = 0,0
        hm = {
            'R': (1, 0),
            'L': (-1, 0),
            'U': (0, 1),
            'D': (0, -1)
        }
        for m in moves:
            a += hm[m][0]
            b += hm[m][1]
        if a == 0 and b == 0:
            return True
        return False