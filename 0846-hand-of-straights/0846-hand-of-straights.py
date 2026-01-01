class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        c = Counter(hand)
        sortc = dict(sorted(c.items()))
        start = next(iter(sortc))
        count = 0
        while sortc:
            if start not in sortc:
                return False
            sortc[start] -= 1
            if sortc[start] == 0:
                del sortc[start]
            start += 1
            count += 1
            if count == groupSize:
                count = 0
                if sortc:
                    start = next(iter(sortc))
        return True