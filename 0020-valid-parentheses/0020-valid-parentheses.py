class Solution:
    def isValid(self, s: str) -> bool:
        bp = {')':'(', '}':'{', ']':'['}
        stack = []
        for v in s:
            if v in bp.keys():
                if not stack:
                    return False
                else:
                    p = stack.pop()
                    if bp[v] == p:
                        continue
                    else:
                        return False
            else:
                stack.append(v)
        if not stack:
            return True
        return False