# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

from queue import Queue
from sys import maxsize
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        ans = maxsize
        gr = [[] for _ in range(n+1)]
        for edge in roads:
            gr[edge[0]].append((edge[1], edge[2])) # u-> {v, dis}
            gr[edge[1]].append((edge[0], edge[2])) # v-> {u, dis}

        vis = [0] * (n+1)
        q = Queue()
        q.put(1)
        vis[1] = 1
        while not q.empty():
            node = q.get()
            for v, dis in gr[node]:
                ans = min(ans, dis)
                if vis[v] == 0:
                    vis[v] = 1
                    q.put(v)

        return ans