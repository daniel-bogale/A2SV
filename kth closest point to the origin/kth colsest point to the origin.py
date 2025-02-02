import math
class Solution((object)):
    def kClosest(self, points,k):

        points.sort(key = lambda x : x[0]**2 + x[1]**2)
        output = []
        for i in range(k):
            output.append(points[i])

        return output
