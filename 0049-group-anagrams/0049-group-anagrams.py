from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for v in word:
                key[ord(v) - ord('a')] += 1
            k = tuple(key)
            res[k].append(word)
        return list(res.values())
            