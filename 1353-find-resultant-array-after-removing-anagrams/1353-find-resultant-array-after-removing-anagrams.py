class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def sig(word):
            count = [0] * 26
            for c in word:
                count[ord(c) - 97] += 1
            return tuple(count)
        result, prev = [], None
        for word in words:
            s = sig(word)
            if prev != s:
                result.append(word)
                prev = s
        return result