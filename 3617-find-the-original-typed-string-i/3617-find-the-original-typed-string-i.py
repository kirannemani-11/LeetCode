class Solution:
    def possibleStringCount(self, word: str) -> int:
        c = 0
        prev = ""
        for v in word:
            if v == prev:
                c+=1
            else:
                prev = v
        return c+1