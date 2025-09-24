# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = {i: i for i in range(n)}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]] 
                x = parent[x]
            return x

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union(i, j)

        roots = {find(i) for i in range(n)}
        return len(roots)
