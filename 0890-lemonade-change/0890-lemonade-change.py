class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for v in bills:
            if v == 5:
                fives += 1
            elif v == 10:
                if fives:
                    fives -= 1
                    tens += 1
                else:
                    return False
            else:
                if tens and fives:
                    tens -= 1
                    fives -= 1
                elif not tens and fives >= 3:
                    fives -= 3
                else:
                    return False
        return True