
class Solution(object):
    def maxArea(self, height):
        
        leftPole = 0
        rightPole = len(height)-1
        MaxArea = 0

        while leftPole < rightPole:
            newArea =(max(leftPole,rightPole)-min(leftPole,rightPole))*(min(height[leftPole],height[rightPole]))
            if MaxArea < newArea:
                MaxArea = newArea
            if height[leftPole]<height[rightPole]:
                leftPole+=1
            else:
                rightPole-=1
        
        return MaxArea
