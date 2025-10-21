class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        mp = Counter(nums)
        keys = list(mp.keys())
        keys.sort()
        freq, ans = 0, 0
        i,j = 0, 0
        for key in range(keys[0], keys[-1]+1):
            while j < len(keys) and keys[j] <= key + k:
                freq += mp[keys[j]]
                j += 1
            while i < len(keys) and keys[i] < key - k:
                freq -= mp[keys[i]]
                i += 1
            ans = max(ans, min(mp.get(key,0)+numOperations, freq))
        return ans