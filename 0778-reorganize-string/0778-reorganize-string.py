import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        pq = [(-freq,char) for char, freq in Counter(s).items()]
        heapq.heapify(pq)
        prev = (0, '')
        r = []
        while pq or prev[0] < 0:
            if not pq and prev[0] < 0:
                return ""
            freq, char = heapq.heappop(pq)
            if char != prev[1]:
                r.append(char)
                if prev[0] < 0:
                    heapq.heappush(pq, prev)
            prev = (freq+1, char)
        return ''.join(r)