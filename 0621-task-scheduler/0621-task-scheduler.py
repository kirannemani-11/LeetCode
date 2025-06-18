import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        units = []
        cooldown = []
        c = Counter(tasks)
        for v in c.items():
            heapq.heappush(units, (-v[1], v[0]))
        time = -1
        while units or cooldown:
            time+=1
            while cooldown and cooldown[0][0] <= time:
                cd, v, c = heapq.heappop(cooldown)
                if c > 0:
                    heapq.heappush(units, (-c, v))
            if units:
                c, v = heapq.heappop(units)
                c = -c - 1
                if c > 0:
                    heapq.heappush(cooldown ,(time+n+1,v,c))
        return time + 1