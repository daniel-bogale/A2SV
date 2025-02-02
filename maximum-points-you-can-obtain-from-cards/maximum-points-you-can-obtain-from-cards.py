class Solution(object):
    def maxScore(self, cardPoints, k):
        l=0
        r=len(cardPoints)-k
        total=sum(cardPoints[r:])
        answer=total
        while r<len(cardPoints):
            total+=cardPoints[l]-cardPoints[r]
            answer=max(answer,total)
            r+=1
            l+=1
        return answer
