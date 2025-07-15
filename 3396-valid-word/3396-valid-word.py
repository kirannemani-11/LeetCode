class Solution:
    def isValid(self, word: str) -> bool:
        vo = False
        con = False
        vow = ['a','e','o','i','u']
        for v in word:
            if v.isalpha():
                if v.lower() in vow:
                    vo = True
                else:
                    con = True
            elif v.isdigit():
                continue
            else:
                return False
        if len(word) >= 3 and vo and con:
            return True
        return False