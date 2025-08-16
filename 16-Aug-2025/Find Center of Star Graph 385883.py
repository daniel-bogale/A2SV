# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dir = defaultdict(int)

        for e in edges:
            dir[e[0]] += 1
            dir[e[1]] += 1

        for k , val in dir.items():
            if val == len(edges):
                return k

        return -1  