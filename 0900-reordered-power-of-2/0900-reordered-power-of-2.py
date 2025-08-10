class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        value = "".join(sorted(str(n)))
        length = len(value)
        power = 1
        while len(str(power)) <= length:
            if len(str(power)) == length:
                if ''.join(sorted(str((power)))) == value:
                    return True
            power <<= 1
        return False