class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = set()
        maxfreq = 0
        left = 0
        for right in range(len(s)):
            while s[right] in freq:
                freq.remove(s[left])
                left += 1
                if s[right] not in freq:
                    break
            freq.add(s[right])
            maxfreq = max(maxfreq, len(freq))
        return maxfreq