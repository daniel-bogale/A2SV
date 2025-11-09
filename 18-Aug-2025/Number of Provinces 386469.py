# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        visited = set()
        
        def dfs(city):
            for adj_city in range(n):
                if isConnected[city][adj_city] == 1 and adj_city not in visited:
                    visited.add(adj_city)
                    dfs(adj_city)
        
        provinces = 0
        for city in range(n):
            if city not in visited:
                visited.add(city)
                dfs(city)
                provinces += 1
        
        return provinces