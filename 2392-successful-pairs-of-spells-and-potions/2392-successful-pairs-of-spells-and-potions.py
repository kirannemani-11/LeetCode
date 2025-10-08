class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []
        for s in spells:
            if s == 0:
                result.append(0)
            else:
                pairs = 0
                low = 0
                high = len(potions) - 1
                while low <= high:
                    mid = (low + high) // 2
                    if s * potions[mid] >= success:
                        pairs = max(pairs, len(potions) - mid)
                        high = mid - 1
                    else:
                        low = mid + 1 
            result.append(pairs)
        return result