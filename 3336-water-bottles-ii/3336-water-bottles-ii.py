class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        totBot = numBottles
        emptyBot = numBottles
        while emptyBot > numExchange - 1:
            emptyBot -= numExchange - 1
            totBot += 1
            numExchange += 1
        return totBot