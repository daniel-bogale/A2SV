# Problem: Minimize Hamming Distance After Swap Operations - https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        res = n = len(source)
        G = [set() for i in range(n)]
        for i, j in allowedSwaps:
            G[i].add(j)
            G[j].add(i)
        seen = [0] * n

        def dfs(i):
            seen[i] = 1
            found.append(i)
            for j in G[i]:
                if not seen[j]:
                    dfs(j)

        for i in range(n):
            if seen[i]: continue
            found = []
            dfs(i)
            count1 = collections.Counter(source[j] for j in found)
            count2 = collections.Counter(target[j] for j in found)
            res -= sum((count1 & count2).values())
        return res
        