# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total_boomerangs = 0
        for p1 in points:
            distance_count = {}
            for p2 in points:
                if p1 == p2:
                    continue
                distance = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
                distance_count[distance] = distance_count.get(distance, 0) + 1
            for count in distance_count.values():
                total_boomerangs += count * (count - 1)
        return total_boomerangs