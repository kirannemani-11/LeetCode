class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) <= k:
            temp = ""
            for v in word:
                nc = chr(ord(v)+1) if v != 'z' else 'a'
                temp += v + nc
            word = temp
        return word[k-1]