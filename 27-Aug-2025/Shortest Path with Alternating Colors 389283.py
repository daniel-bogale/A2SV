# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

from collections import defaultdict
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)

        for src, dst in redEdges:
            red[src].append(dst)
        for src, dst in blueEdges:
            blue[src].append(dst)
        
        result = [-1 for i in range(n)]

        q = deque()
        q.append([0, 0, None]) 

        visited = set()
        visited.add((0,None))

        while q: 
            node, length, edgeColor = q.popleft()
            if result[node] == -1:
                result[node] = length

            if edgeColor != "RED":
                for nei in red[node]:
                    if (nei, "RED") not in visited:
                        visited.add((nei,"RED"))
                        q.append([nei, length+1, "RED"])

            if edgeColor != "BLUE":
                for nei in blue[node]:
                    if (nei, "BLUE") not in visited:
                        visited.add((nei,"BLUE"))
                        q.append([nei, length+1, "BLUE"])

        return result