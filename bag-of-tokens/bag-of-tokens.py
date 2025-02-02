class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        result=score=0
        left,right=0,len(tokens)-1
        tokens.sort()
        while left<=right:
            if tokens[left]<=power:
                score+=1
                result=max(result,score)
                power-=tokens[left]
                left+=1
            else:
                if score>0:
                    power+=tokens[right]
                    score-=1
                    right-=1
                else:
                    break
        return result
