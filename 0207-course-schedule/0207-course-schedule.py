from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        for v in prerequisites:
            graph[v[1]].append(v[0])
            in_degree[v[0]] += 1
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        topo = []
        while q:
            i = q.popleft()
            topo.append(i)
            for v in graph[i]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        if len(topo) == numCourses:
            return True
        return False