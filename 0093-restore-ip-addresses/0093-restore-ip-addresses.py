class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def bt(curr, i):
            if len(curr) == 4:
                if i == len(s):
                    res.append(".".join(curr))
                return
            for l in range(1,4):
                if i + l > len(s):
                    break
                part = s[i: i+l]
                if len(part) > 1 and part[0] == '0':
                    continue
                elif int(part) > 255:
                    continue
                curr.append(part)
                bt(curr, i+l)
                curr.pop()
        bt([],0)
        return res