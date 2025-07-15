from collections import deque
from collections import defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outDegree = [0] * len(graph)
        g = defaultdict(list)
        for i,vals in enumerate(graph):
            outDegree[i] += len(vals)
            for v in vals:
                g[v].append(i)
        q = deque([i for i,v in enumerate(outDegree) if v == 0])
        topo = []
        while q:
            i = q.popleft()
            topo.append(i)
            for v in g[i]:
                outDegree[v] -= 1
                if outDegree[v] == 0:
                    q.append(v)
        return sorted(topo)