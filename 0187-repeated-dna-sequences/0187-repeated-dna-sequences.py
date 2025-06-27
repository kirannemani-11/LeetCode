class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        ans = set()
        for i in range(0,len(s)-9):
            v = s[i:i+10] 
            if v not in seen:
                seen.add(v)
            else:
                ans.add(v)
        return list(ans)