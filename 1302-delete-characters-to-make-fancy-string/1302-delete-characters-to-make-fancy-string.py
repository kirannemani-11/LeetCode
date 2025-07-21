class Solution:
    def makeFancyString(self, s: str) -> str:
        prev = s[0]
        c = 1
        r = "" + prev
        for i in range(1, len(s)):
            if s[i] != prev:
                prev = s[i]
                c = 1
                r += s[i]
            else:
                c += 1
                if c <= 2:
                    r += s[i]
        return r