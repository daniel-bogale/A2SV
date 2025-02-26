# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        boomerang_count = 0
        for i in range(len(points)):
            distance_from_i = {}
            for j in range(len(points)):
                if i == j:
                    continue
                dis = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
                distance_from_i[dis] = distance_from_i.get(dis,0)+1
            boom_i = 0
            for val in distance_from_i.values():
                if val > 1:
                    boom_i += val*(val-1)
            boomerang_count +=boom_i
        return boomerang_count       