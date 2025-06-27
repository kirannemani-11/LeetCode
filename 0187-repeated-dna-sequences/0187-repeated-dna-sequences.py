class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        ans = set()
        for i in range(0,len(s)-9):
            if s[i:i+10] not in seen:
                seen.add(s[i:i+10])
            else:
                ans.add(s[i:i+10])
        return list(ans)